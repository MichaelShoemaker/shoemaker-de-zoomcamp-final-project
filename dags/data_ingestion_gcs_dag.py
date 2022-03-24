import os
import logging
from datetime import datetime

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


from google.cloud import storage
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateExternalTableOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryDeleteTableOperator



import pandas as pd
import pyarrow as pa
import pyarrow.csv as pv
import pyarrow.parquet as pq

PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
BUCKET = os.environ.get("GCP_GCS_BUCKET")

#https://divvy-tripdata.s3.amazonaws.com/202202-divvy-tripdata.zip

dataset_zip = "{{ execution_date.strftime(\'%Y%m\') }}-divvy-tripdata.zip"
csv_file = "{{ execution_date.strftime(\'%Y%m\') }}-divvy-tripdata.csv"
dataset_url = f"https://divvy-tripdata.s3.amazonaws.com/{dataset_zip}"
path_to_local_home = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")
parquet_file = csv_file.replace('.csv', '.parquet')
BIGQUERY_DATASET = os.environ.get("BIGQUERY_DATASET", 'divvy_trips_data')


def format_to_parquet(src_file):
    if not src_file.endswith('.csv'):
        logging.error("Can only accept source files in CSV format, for the moment")
        return
    df = pd.read_csv(src_file)
    df.started_at = pd.to_datetime(df.started_at)
    df.ended_at = pd.to_datetime(df.ended_at)
    df.start_station_id = df.start_station_id.astype(str)
    df.end_station_id = df.end_station_id.astype(str)

    table = pa.Table.from_pandas(df)
    pq.write_table(table, 'file_name.parquet')

    pq.write_table(table, src_file.replace('.csv', '.parquet'))


# NOTE: takes 20 mins, at an upload speed of 800kbps. Faster if your internet has a better upload speed
def upload_to_gcs(bucket, object_name, local_file):
    """
    Ref: https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-python
    :param bucket: GCS bucket name
    :param object_name: target path & file-name
    :param local_file: source path & file-name
    :return:
    """
    # WORKAROUND to prevent timeout for files > 6 MB on 800 kbps upload speed.
    # (Ref: https://github.com/googleapis/python-storage/issues/74)
    storage.blob._MAX_MULTIPART_SIZE = 5 * 1024 * 1024  # 5 MB
    storage.blob._DEFAULT_CHUNKSIZE = 5 * 1024 * 1024  # 5 MB
    # End of Workaround

    client = storage.Client()
    bucket = client.bucket(bucket)

    blob = bucket.blob(object_name)
    blob.upload_from_filename(local_file)


default_args = {
    "owner": "airflow",
    "depends_on_past": True,
    "retries": 1,
}

# NOTE: DAG declaration - using a Context Manager (an implicit way)
with DAG(
    dag_id="data_ingestion_gcs_dag1",
    schedule_interval="0 20 15 * *",
    start_date=datetime(2020, 4, 1),
    default_args=default_args,
    catchup=True,
    max_active_runs=1,
    tags=['dtc-de'],
) as dag:

    download_dataset_task = BashOperator(
        task_id="download_dataset_task",
        bash_command=f"curl -sSL {dataset_url} > {path_to_local_home}/{dataset_zip}"
    )

    unzip_data_file = BashOperator(
        task_id = "unzip_data_file",
        bash_command = f"cd /opt/airflow && unzip {path_to_local_home}/{dataset_zip}"
    )


    format_to_parquet_task = PythonOperator(
        task_id="format_to_parquet_task",
        python_callable=format_to_parquet,
        op_kwargs={
            "src_file": f"{path_to_local_home}/{csv_file}",
        },
    )


    clean_up_files = BashOperator(
        task_id = "clean_up_files",
        bash_command = 'cd /opt/airflow && rm *.zip *.csv && rm -rf __MACOS*'
    )

    local_to_gcs_task = PythonOperator(
        task_id="local_to_gcs_task",
        python_callable=upload_to_gcs,
        op_kwargs={
            "bucket": BUCKET,
            "object_name": f"raw/{parquet_file}",
            "local_file": f"{path_to_local_home}/{parquet_file}",
        },
    )
    
    delete_table = BigQueryDeleteTableOperator(
        task_id="delete_table",
        deletion_dataset_table=f"{PROJECT_ID}.{BIGQUERY_DATASET}.external_table",
    )


    bigquery_external_table_task = BigQueryCreateExternalTableOperator(
        task_id="bigquery_external_table_task",
        table_resource={
            "tableReference": {
                "projectId": PROJECT_ID,
                "datasetId": BIGQUERY_DATASET,
                "tableId": "external_table",
            },
            "externalDataConfiguration": {
                "sourceFormat": "PARQUET",
                "sourceUris": [f"gs://{BUCKET}/raw/*.parquet"],
            },
        },
    )

    download_dataset_task >> unzip_data_file >> format_to_parquet_task >> clean_up_files >> local_to_gcs_task >> delete_table >> bigquery_external_table_task


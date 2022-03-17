# Final Project for Data Engineering Zoom Camp
---
Final Project for de-zoomcamp 2022 (1st cohort)


# PROJECT:
---
This project will aggregate historical Divvy Bike Data from the City of Chicago.

# Problem Description:
---
While this data is freely available from the City of Chicago it is divided by month and is in csv format. 
- By combining this data there may be trends that can be identified which may otherwise be missed looking at a smaller subset of the data. 
- Creating a resilient data pipeline to facilitate the importing and aggregation of the data this project should be of utility for someone who wishes to perform the same task while eliminating the need for repetitive data cleaning and importing.

# Data:
---
The data to be used for this project can be found here - [Divvy Bike Data](https://divvy-tripdata.s3.amazonaws.com/index.html)

Below is a sample of the data to be used:
![Screenshot](/images/DataSample-FinalProject.png)

# Technologies to be Used:
---
- GCP VM Instance (Processing)
- Terraform (Infrascructure as a Service)
- Airflow (Data Pipeline - ETL)
- GCP Storage Bucket (Data Lake)
- Big Query (Data Warehouse)
- DBT (Creating Analytical Views)

# Project:
---
Final Project for de-zoomcamp 2022 (1st cohort)


# Project Summary:
---
This project will aggregate historical Divvy Bike Data from the City of Chicago.

# Technologies to be Used:
---
- GCP VM Instance (Processing)
- Terraform (Infrascructure as a Service)
- Airflow (Data Pipeline - ETL)
- GCP Storage Bucket (Data Lake)
- Big Query (Data Warehouse)
- DBT (Creating Analytical Views)

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

ride_id - Unique ID Assigned to Each Divvy Trip<br>
rideable_type - Type of Vehicle Used<br>
started_at - Start of Trip Date and Time<br>
ended_at - End of Trip Date and Time<br>
start_station_name - Name Assigned to Station the Trip Started at<br>
start_station_id - Unique Identification Number of Station the Trip Started at<br>
end_station_name - Name Assigned to Station the Trip Ended at<br>
end_station_id - Unique Identification Number of Station the Trip Ended at<br>
start_lat - Latitude of the Start Station<br>
start_lng - Longitude of the Start Station<br>
end_lat - Latitude of the End Station<br>
end_lng - Longitude of the End Station<br>
member_casual - Field with Two Values Indicating Whether the Rider has a Divvy Membership or Paid with Credit Card<br>

#Data Pipeline Diagram:
---
TODO

# Proposed Data Visualizations
---
TODO

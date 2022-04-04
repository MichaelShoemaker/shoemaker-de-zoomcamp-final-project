# Create the VM
---
Start in your GCP Account. At the top click the projects drop down and then select +New Project
![NewProjectGCP](https://user-images.githubusercontent.com/7443591/160303897-0491326d-90c5-4be2-8189-1347c0d1955a.png)<br>

You can call the project whatever you would like. We will need to use this name later.
![NameProject](https://user-images.githubusercontent.com/7443591/160303944-c85df7fd-3d34-4e09-80fa-690cec7f274a.png)<br>

Once the new project has been created click the project drop down again and switch to the new project you just created.
![SwitchToNewProject](https://user-images.githubusercontent.com/7443591/160303955-10725499-016a-49a0-a75e-2d2a172af1c0.png)<br>

Click the hamburger icon in the top left and scroll down to Compute Engine. Choose VM instances.
![SelectComputeEngine](https://user-images.githubusercontent.com/7443591/160303984-5d5d2f1a-5375-446c-b3de-162c10f59b16.png)<br>

Click to Enable for the Compute Engine API. This will take a few moments.
![EnableCloudComputeAPI](https://user-images.githubusercontent.com/7443591/160304015-1359de1b-d1f5-45cf-b1af-29f50c365e44.png)<br>

Once it has finished you can now click Create at the bottom. 
![CreateInstance](https://user-images.githubusercontent.com/7443591/160304046-1b12ad3a-f0e4-4a81-ab03-2478ab03c3ec.png)<br>

Select the Region closest to you. Look for a green leafe icon if you want to be eco-friendly. Choose e2-standard-4 for the Machine Type
![VM_RegionAndType](https://user-images.githubusercontent.com/7443591/160304100-7b788c40-f5a9-401f-b341-96c95791a802.png)<br>

Scroll down to the Boot disk section and click the Change button. 
![ChangeBootDisk](https://user-images.githubusercontent.com/7443591/160304137-b76e369c-6718-4567-be4c-4f2f685adbd7.png)<br>

Select the options shown here and click Select

![ChangeOS](https://user-images.githubusercontent.com/7443591/160304150-d4e7ea43-8ab5-4a9f-ad5f-87bb2aa9f2c1.png)<br>

Scroll down to the bottom and click Create. 
![CreateOSButton](https://user-images.githubusercontent.com/7443591/160304196-94dc834c-0d76-493e-8011-b6d5c190c4d5.png)<br>

# Create Service Account
---
In GCP scroll down to IAM & Admin and select IAM<br>
![IAM](https://user-images.githubusercontent.com/7443591/160307298-2d6f0f75-179d-4110-8eaf-5a88437cd39c.png)<br>


Scroll down to Service Accounts<br>
![ServiceAccount](https://user-images.githubusercontent.com/7443591/160307321-c48b5677-9f11-43cc-9a9c-c6a168b43de5.png)<br>

Select Create Service Account<br>
![CreateServiceAccount](https://user-images.githubusercontent.com/7443591/160307333-a1975b81-eb75-47cf-ab0d-917dbdece8e4.png)<br>

Name it whatever you would like and click Create and Continue<br>
![NameServiceAccount](https://user-images.githubusercontent.com/7443591/160307376-bb4f191e-3a02-43b0-955b-cd8094163cf7.png)<br>

Give the service account the following roles<br>
![serviceAccountRoles](https://user-images.githubusercontent.com/7443591/160307396-10560756-84cd-489e-9dbe-e2d05e22d8dc.png)<br>

Click continue and then done. You should now see the service account. Click the three dot elipse on the right hand side and choose manage keys.<br>
![ManageKeys](https://user-images.githubusercontent.com/7443591/160307479-af264fdc-5500-440e-bef1-c0773541091b.png)<br>

Choose Add Key then Create New Key<br>
![AddKey](https://user-images.githubusercontent.com/7443591/160307539-aa50578a-514c-4e6a-9483-9a24353e544c.png)<br>

Click create and it will download the .json key to your computer<br>
![CreateKey](https://user-images.githubusercontent.com/7443591/160307568-b6bfcb42-d053-432a-8982-374c9b23f1da.png)<br>


# Setup SSH to VM
---
In your terminal run the command<br>
```ssh-keygen -t rsa -f ~/.ssh/<whatever you want to call your key> -C <the username that you want on your VM> -b 2048```
<br>
ex:
```ssh-keygen -t rsa -f ~/.ssh/gcp -C john -b 2048```

Once the command runs succesfully cd to the .ssh directory. Cat the contents of the <whatever you called your key>.pub. Copy the output to your clipboard.

In GCP click the hamburger icon again and scroll down to select Metadata
![Metadata](https://user-images.githubusercontent.com/7443591/160304715-63365049-f62c-4ad0-beef-48571a2abfb5.png)<br>
  
Select SSH Key and then click ADD SSH KEY.
![SelectAddSSHKey](https://user-images.githubusercontent.com/7443591/160304738-c1859228-b734-49eb-a68c-a0c7b1fd21b5.png)<br>
  
Paste the public key you copied into the blank provided and then click save.
![SSH_PasteAndSave](https://user-images.githubusercontent.com/7443591/160304842-5f4a2d15-51fc-48e3-92dc-1ae49b8ec3c2.png)

Go to the VM, check the check box and press start if it's not already running. Copy the External IP address that is displayed once it starts. You can then create a config file in your .ssh directory and add the following entry:<br>


![StartVMExternalIP](https://user-images.githubusercontent.com/7443591/160305325-562a85f4-a079-424a-99d9-2f716cb7ca41.png)

  
```
  Host <name to use when connecting
    HostName <public IP address>
    User <User name you chose when running the ssh-keygen command>
    IdentityFile /home/<local user name>/.ssh/<your private key>
```

# Connecting and setting up
---
Install Visual Studio Code if you don't have it already. Search Extensions for SSH and install Remote-SSH from Microsoft.
  
![InstallSSHExtension](https://user-images.githubusercontent.com/7443591/160305404-99508aa5-82fd-46a1-9e09-c1061a5f378d.png)<br>
  
  
Then in the lower left hand corner click the green icon to Open a Remote Window.
![OpenARemoteWindow](https://user-images.githubusercontent.com/7443591/160305492-d771aee3-3c50-4790-b9e1-e9f0a89109ad.png)<br>
  

Then at the top choose Connect to Host and choose the name you gave the VM in the config file. Just click continue if it prompts you.
![ConnectToHost](https://user-images.githubusercontent.com/7443591/160305604-eeef8024-b846-46f9-8cd0-ee4eb394d9be.png)<br>
  
  
Press Ctrl + ` <the key by the number 1 on your key > to open a terminal window.
![OpenATerminal](https://user-images.githubusercontent.com/7443591/160305803-82c447a5-ec61-4525-8107-31a4560536cb.png)<br>
  
Download the latest version of Anaconda with wget.
![WgetAnaconda](https://user-images.githubusercontent.com/7443591/160305821-c3fd292d-8d90-40d6-b965-71f2a85134d5.png)<br>
  
Make the download an executable and run it.
![InstallAnaconda](https://user-images.githubusercontent.com/7443591/160305843-927d47d9-41b7-4e99-82fa-cb22022113cf.png)<br>
  
Just hold down enter through the terms of service until it prompts you to type yes.
![YesToInstallAnaconda](https://user-images.githubusercontent.com/7443591/160305850-f228525f-1558-427d-a197-755aef8a70c9.png)

First update with<br>
```sudo apt-get update```
  
Install docker with<br>
```sudo apt install docker.io```

Clone this repo<br>
```git clone https://github.com/MichaelShoemaker/shoemaker-de-zoomcamp-final-project.git```
  
Make a bin directory with and switch to it<br>
```
mkdir bin
cd bin
```
  
Download docker-compose<br>
``` wget https://github.com/docker/compose/releases/download/v2.3.4/docker-compose-linux-x86_64 -O docker-compose```
  
Make it execuatable<br>
```chmod +x docker-compose```
  

Add docker-compose to path in your .bashrc file<br>

![modbashrc](https://user-images.githubusercontent.com/7443591/160306744-c50d5324-e523-4709-921e-2be484cf0f0e.png)

![AddComposeToPath](https://user-images.githubusercontent.com/7443591/160306747-08b16b41-a22d-41d7-b704-258770a3fc20.png)

Update your path by running<br>
```source .bashrc```

Load your .json file for your service account. It is most likely in your Downloads directory. Cd to Downloads, ssh to your vm, run sftp and then run
```put <you file>.json```
  
Exit sftp, ssh back to your VM, make a directory called .google/credentials in your home directory and move the file there<br>
  
```
  mkdir -p .google/credentials
  cp <your service account json file>  .google/credentials/google_credentials.json
```

You should also add the following to your .bashrc file<br>
export GOOGLE_APPLICATION_CREDENTIALS=~/.google/credentials/google_credentials.json<br>
and then run<br>
```source .bashrc```
  
Now authenticate by running<br>
gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS<br>
  
Install terrraform by running these commands<br>
```
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
sudo apt-get update && sudo apt-get install terraform
```
Go to shoemaker-de-zoomcamp-final-project/terraform directory. There is one thing you must update and two you probably want to.<br>
The project name you MUST change to match your project name<br>
The Region is okay if you are in the US, but make sure you choose a region that is Multi<br>
The data_lake_bucket name. This will be the name of the bucket that will store our files<br>
The BQ_DATASET Default will be the name of your dataset in Big Query<br>
![ChangeTerraform](https://user-images.githubusercontent.com/7443591/160309612-77a3eb67-474b-41ab-a7c9-618ff574953c.png)<br>

Run the commands<br>
```
terraform init
terraform apply
```
When it prompts you just type "yes"

# Running Airflow

Run:
sudo usermod -aG docker $USER<br>
newgrp docker<br>

Ctrl + d to exit your ssh session<br>
log back<br>
Go to shoemaker-de-zoomcamp-final-project and update the values shown below in the docker-compose file to match your environment<br>
![ChangeDockerComposeVariables](https://user-images.githubusercontent.com/7443591/160399379-4d6c63ae-35f3-4abb-9a75-cc07beb22700.png)

Also run the below command to copy your credentials to where docker-compose can use them.
In your home directory run:<br>
```
mkdir -p .google/credentials
sudo cp .gc/reproduce-de-project-c7d579a009f9.json .google/credentials/google_credentials.json
```
Go back to shoemaker-de-zoomcamp-final-project and run<br>
```
docker-compose build
docker-compose up airflow-init
```
  
This will take a while the first time. You might want to grab a cup of coffee or lunch.<br> 
  
in Visual Studio code click on ports and forward port 8080<br>
  ![ForwardPort](https://user-images.githubusercontent.com/7443591/160403735-7c40babc-7d63-4b51-90da-c065e5b254a0.png)

go to localhost:8080<br>
  
and login with airflow airflow for the credentials<br>
![AirflowLogin](https://user-images.githubusercontent.com/7443591/160413081-4f4e606f-09f6-4d4f-9b94-5241f37091a6.png)

Enable the dag and you should see it run. It takes 10-15 minutres to run all of the run. After it has completed you should see the partquet files in your GCP Bucket.
 ![DagRunning](https://user-images.githubusercontent.com/7443591/160413468-d5f236a2-0a72-46b5-bab0-605196e3efd4.png)
 
  
  ![ParquetBucket](https://user-images.githubusercontent.com/7443591/160413881-5252646a-2b2c-4a05-8d8e-ce2ba8bcd52d.png)

  

# Big Query Table Creation
Once Airflow has created all of your files in your storage bucket go to Big Query and run<br>
  
```
  CREATE OR REPLACE EXTERNAL TABLE <your project>.<your dataset>.external_divvy_data
options(
    format = 'parquet',
    uris = ['<path to your storage bucket>/raw/*.parquet']
)
```

Then create your partitioned table with<br>
```
CREATE OR REPLACE TABLE  `<your project>.<your dataset>.divvy_data_partitioned` 
PARTITION BY
    DATE(started_at) 
CLUSTER BY start_station_name
    AS 
SELECT * FROM `<your project>.<your dataset>.external_divvy_data` 
```  
# Transform data with DBT
Go to https://github.com/MichaelShoemaker/dbt-de-zoomcamp and fork the repository.<br>

In to Account Settings and select new project.<br>
![dbt_accountsettings](https://user-images.githubusercontent.com/7443591/161543430-127658c0-560b-4c4b-b942-b7b8182d726c.png)<br>
  
![dbt_newproject](https://user-images.githubusercontent.com/7443591/161543459-804b93aa-b529-4609-85e5-d6de6a0ba213.png)<br>
  
Click Begin<br>
![dbt_begin](https://user-images.githubusercontent.com/7443591/161543524-bf08613e-3138-4abd-b78c-50d3588aecc6.png)

Name the project whatever you like<br>
  
![dbt_name](https://user-images.githubusercontent.com/7443591/161543589-b69283d2-2dcd-410b-8ea5-aa175050376d.png)

Select Big Query<br>
 ![dbt_bigquery](https://user-images.githubusercontent.com/7443591/161543760-768c4ebc-4fa6-411e-8cde-d90fd9818975.png)

Use the service account json file from our GCP Project<br>

![dbt_json](https://user-images.githubusercontent.com/7443591/161543875-37bdca46-a850-43bf-80f5-2011c2b410da.png)

Choose git clone and paste the ssh link from your github fork<br>
  
![dbt_gitclone](https://user-images.githubusercontent.com/7443591/161543959-3bf65d77-57f2-4310-b751-6fff6f3750d5.png)



You can create a new project in dbt. Fork this repo https://github.com/MichaelShoemaker/final_project_dbt and then use it in dbt.
  
# Analytics Reports
---
Here are the tiles that were created for this project:
https://datastudio.google.com/reporting/ea3f603a-f8f5-4d0c-9664-7608835b8ddb/page/0ttoC
  

See below options on the left below for reference to build the reports:

#TIME SERIES
  ![TimeSeries](https://user-images.githubusercontent.com/7443591/160406733-270f06b3-5fb8-4cc9-9953-0743a6a545d8.png)<br>

#STATON BAR GRAPH
  ![barGraph](https://user-images.githubusercontent.com/7443591/160406769-8a022861-1b1f-4cd9-b38f-06f480d921b6.png)<br>
  
#USER BREAKDOWN BAR GRAPH RIDE COUNT
  ![barBreakDown](https://user-images.githubusercontent.com/7443591/160406797-473c3cb4-5b39-4471-bf33-fd99047a3600.png)<br>




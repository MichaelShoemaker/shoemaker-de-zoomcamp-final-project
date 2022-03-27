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


# Set up SSH to VM
---
In your terminal run the command<br>
```ssh-keygen -t -rsa -f ~/.ssh/<whatever you want to call your key> -C <the username that you want on your VM> -b 2048```
<br>
ex:
```ssh-keygen -t -rsa -f ~/.ssh/gcp -C john -b 2048```

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
![OpenARemoteWindow](https://user-images.githubusercontent.com/7443591/160305450-248908f1-0fb0-424d-87b6-c0ac7107bad6.png)






# mqtt_demo
Mqtt demo which can take a pic from a remote location and send it back to us

MQTT Application Documentation:

Hardware required: Hikey 970, USB Video Camera, PC

Pre-requisites for PC and Hikey970:

sudo apt-get update
sudo apt-get install python-dev python-pip fswebcam 
pip install paho-mqtt

Perform the following steps for the MQTT Demo:

Step 1:

Run the mqtt_client_publish python script on Hikey970 

python mqtt_client_publish.py

Step 2:

Run the mqtt_client_demo python script on PC

python mqtt_client_demo.py

Step 3:

Run the mqtt_publish_demo python script next on the PC

python mqtt_publish_demo.py

It will ask you for an input. 
Enter capture 

This will capture an image from Hikey 970 and send it back to the PC. Make sure the USB camera is connected to Hikey970. 



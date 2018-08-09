# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish

print("please enter msg:")
msg = raw_input()
publish.single("nishant/test", msg, hostname="test.mosquitto.org")
print("Done")
 

import time
import paho.mqtt.client as paho
from datetime import datetime
broker="broker.mqttdashboard.com"

#define callback
def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))
    

client= paho.Client("clientId-7OAVvZj3RG",8000) #ch = client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
######Bind function to callback
client.on_message=on_message
#####
print("connecting to broker ",broker)
client.connect(broker)#connect
client.loop_start() #start loop to process received messages
print("subscribing ")
client.subscribe("IoTassignment_revanth")#subscribe
time.sleep(2)
print("publishing ")
now=datetime.now()

dt=now.strftime("""now: %d:%m:%Y,%H:%M:%S,
                   name: Revanth""")


client.publish("IoTassignment_revanth",dt)#publish
time.sleep(4)
client.disconnect() 
 

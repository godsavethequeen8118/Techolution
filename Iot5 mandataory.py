import time
from machine import Pin
from MQ135 import MQ135
import paho.mqtt.client as paho
import network
SSID="Revanth"
Pass="qwertyuiop"
broker="broker.mqttdashboard.com"
client=paho.Client("clientId-7OAVvZj3RG",8000)\
        
m=MQ135(0)
def do_connect():
    wlan=network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(SSID,Pass)
        while not wlan.isconnected():
            pass
while True:
    ppm=m.get_ppm()
    
    do_connect()
    client.connect(broker)
    if(ppm>1000):
        client.subscribe("co2")
        client.publish("co2","excess")
        client.disconnect()
    

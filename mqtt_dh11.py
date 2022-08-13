#!/bin/env/ python3

import sys
import paho.mqtt.client as mqtt
import Adafruit_DHT
import time

broker_address="10.0.0.9"

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('Usage: sudo ./Adafruit_DHT.py [11|22|2302] <GPIO pin number>')
    print('Example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO pin #4')
    sys.exit(1)

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

def on_log(client, userdata, level, buf):
    print("log: ",buf)

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    print("creating new instance")
    client = mqtt.Client("P1") #create new instance
    print("connecting to broker")
    client.username_pw_set(username="mqtt",password="publishme$")
    client.connect(broker_address) #connect to broker
    client.loop_start() #start the loop
    print("Subscribing to topic","house/pizero/temperature")
    client.subscribe("house/pizero/temperature")
    print("Publishing message to topic","house/pizero/temperature")
    client.publish("house/pizero/temperature",temperature)
    print("Subscribing to topic","house/pizero/humidity")
    client.subscribe("house/pizero/humidity")
    print("Publishing message to topic","house/pizero/humidity")
    client.publish("house/pizero/humidity",humidity)
    time.sleep(4) # wait
    client.loop_stop() #stop the loop
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)

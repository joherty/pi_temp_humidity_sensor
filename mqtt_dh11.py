#!/bin/env/ python3

#Simple script to publish temperature and humidity reading from a DHT11, DHT22 or DHT2302 sensor
#to an MQTT broker using a Raspberry Pi
#joherty

#Using Adafruit_DHT and Paho MQTT

import sys
import paho.mqtt.client as mqtt
import Adafruit_DHT
import time

#set MQTT broker address and topics
broker_address="Add broker IP Address"
topic_temperature="house/pi_two/temperature"
topic_humidity="house/pi_two/humidity"

#parse command line parameters for Adafruit_DHT
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

#attempt a sensor reading, 15 attempts (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

#If a reading is obtained, print it, then send readings to MQTT

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
#create new instance
    client = mqtt.Client("P1")
#pass username and password if required, otherwise comment out
#    client.username_pw_set(username="user",password="password")
#connect to broker
    client.connect(broker_address)
#start the loop
    client.loop_start()
#subscribe to the defined topic 
    client.subscribe(topic_temperature)
#publish to the defined topic
    client.publish(topic_temperature,temperature)
#subscribe to the defined topic 
    client.subscribe(topic_humidity)
#publish to the defined topic
    client.publish(topic_humidity,humidity)
    time.sleep(4) # wait
    client.loop_stop() #stop the loop
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)

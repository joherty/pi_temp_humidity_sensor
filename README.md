# pi_temp_humidity_sensor
Using any Raspberry PI and a DHT11, DHT22 or DHT2302 sensor, read and publish data to an MQTT broker.

The DHT11 is a low-cost and popular sensor for measuring temperature and humidity. The device on the module requires 3 connections to the Raspberry Pi : 3,3V ; GND and a GPIO input pin.
Use PIN 4 on the Pi for the GPIO input pin.


## Description

Use any Pi. Ive tested on v1B, v2 and Pi Zero W 

## Getting Started

### Install Dependencies First

* Adafruit-DHT
```
pip install Adafruit-DHT
```
* Paho MQTT
```
pip install paho-mqtt
```

### Adding the script

Clone or copy the project to your pi. I use home/pi/source as my script directory
* Create a source folder and move into it, then clone the project.
```
sudo mkdir /home/pi/source && cd /home/pi/source
```
```
sudo git clone https://github.com/joherty/pi_temp_humidity_sensor.git
```
* Make the shell script executable (this script will launch mqtt_dht.py with the command line arguments 11 and 4)
(11 is to specify the sensor type, in my case a DHT11)
(4 is the GPIO pin used for data)
```
sudo chmod +x mqtt_dht.sh
```
* Edit mqtt_dht.py and add your MQTT broker address by editing the broker_address variable.
* If you are using authentication on your MQTT server, uncomment and add username and password to client.username_pw_set
in mqtt_dht.sh

Open crontab in edit mode
```
sudo crontab -e
```
* Add the following line to run mqtt_dht.sh every min
```
* * * * * (cd /home/pi/source/temp_sensor && /home/pi/source/pi_temp_humidity_sensor/mqtt_dht.sh)
```

### Executing program
The script will run once every min via cron. Temperature and humudity values will be published to your MQTT broker using
the topics defined under topic_temperature and topic_humidity.


## Authors

Contributors names and contact info

joherty


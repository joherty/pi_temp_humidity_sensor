# pi_temp_humidity_sensor
Using any Raspberry PI and a DHT11, DHT22 or DHT2302 sensor, read and publish data to an MQTT broker.

## Description

Use any Pi. Ive tested on v1B, v2 and Pi Zero W 

## Getting Started

### Dependencies

* Adafruit-DHT
* Paho MQTT

### Installing

Clone or copy the project to your pi. I use home/pi/source as my script directory
* Create a source folder and move into it, then clone the project.
```
sudo mkdir /home/pi/source && cd /home/pi/source
```
```
sudo git clone https://github.com/joherty/temp_sensor.git
```
* Make the files executable
```
sudo chmod +x mqtt_dht.sh mqyy_dht.py
```
* Open crontab in edit mode
```
sudo crontab -e
```
* Add the following line to run mqtt_dht.sh every min
```
* * * * * (cd /home/pi/source/temp_sensor && /home/pi/source/temp_sensor/mqtt_dht.sh)
```

### Executing program

* How to run the program
* Step-by-step bullets
```
pip install Adafruit-DHT
```

## Help

Any advise for common problems or issues.
```
pip install paho-mqtt
```

## Authors

Contributors names and contact info

ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)

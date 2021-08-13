# Training the SPIKE AI Puppy Using ThingWorx Analytics 

<img align="right" src="https://user-images.githubusercontent.com/49819466/129408283-baf50b5d-0816-4554-9f97-54a97c3f4f6a.jpeg" width=50% height=50%>

## Overview 
The AI Puppy is the first SPIKE system trained using ThingWorx via the ESP8266 WiFi Dongle. Inclusion of this dongle expands SPIKE functionalities: now, the training and communication to external machine learning platforms can be done locally, whether that be through API calls or a MQTT protocol. 

The puppy consists of 3 motors (2 legs and a tail), an ultrasonic sensor, a color sensor, and a force sensor. Through utilizing ThingWorx Analytics, the puppy was able to be trained to do more complex actions using complex machine learning algorithms, such as neural networks and gradient boosts. Although the code here only covers training the puppy to sit and stand (utilizing 1 sensor), the communication protocols used allowed for up to 9 sensor values (the max amount of port the SPIKE hub has + 3 gyroscope IMU values) to be sent simultaneously to ThingWorx. Additionally, both categorical and continuous predictive models can be created, opening the door to many training possibilties. 

This repository cover two methods of training: 

**Method 1-** calling ThingWorx Analytics services locally on the SPIKE via API calls on the ESP8266 

**Method 2-** triggering the same services using events/subscriptions via MQTT.

## Setup
### The ESP8266 WiFi Dongle
For both methods, the ESP8266 board will be used to give the SPIKE Prime WiFi capabilities. However, the boot.py code will differ depending on which method is being used. Refer to the ESP8266 folder for the specific code and more details. 


## Training

## Demo 


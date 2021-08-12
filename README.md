# Integrating SPIKE Prime Robotics with ThingWorx Analytics 
# Table of Contents
1. [Overview](#Overview)
2. [Equipment](#Equipment)
3. [Setup](#Setup)

## Overview 

<img align="right" src="https://user-images.githubusercontent.com/49819466/128409745-270eaaea-e580-485b-9fd5-d6a1e227b1f7.jpg" width=50% height=50%>

This repository contains ThingWorx and Lego SPIKE Prime code that allows the SPIKE to be trained using the analytics server extension on ThingWorx. 

A simple ball launcher was built and trained using linear regression to better understand how to integrate ThingWorx with SPIKE Prime. Then, more complex methods of training (eg. neural networks, gradient boosts, random forests, etc.) were explored using the SPIKE Prime puppy system, with a MQTT protocol acting as the main communication method between SPIKE and ThingWorx Analytics. 

To the right is a flowchart of the general training process. Although the SPIKE Puppy is featured, the process is applicable to any SPIKE system.

## Equipment/Software
- ThingWorx instance with the following:
  - Analytics Server Extension
  - CSV Parser Extension
  - MQTT Extension
- SPIKE Prime Kit 
- ESP8266 wifi dongle 
  - [Click here](https://quickest-palladium-2e9.notion.site/SPIKE-Prime-Backpacks-31f12415b3ad429fba34956b9d50b49e) to get more info
- [MQTTX](https://mqttx.app/)- a cloud based broker app used as a bridge between SPIKE and ThingWorx 
  - I have not explored other MQTT broker software, but hear that [Mosquitto](https://mosquitto.org/) is reputable
- [LabView IDE](https://github.com/chrisbuerginrogers/ME35_21) (created by Chris Rogers)

## Setup
In addition to the setup provided here, each folder will contain files detailing setups specific to the systems used. [Here](https://drive.google.com/drive/folders/1ASOn0lAOdE_gR4C9Febgn0rY1Nz9imzS?usp=sharing) is a link to a Google Drive with all of the linked resources and more!

The Ball Launcher code was hosted on Google Colab, and the SPIKE Puppy code is both local & through MQTT.

### LabView IDE 
The LabView IDE was used in order to code MicroPython onto the SPIKE Prime and ESP8266 either through micro USB communication (applicable for both) or bluetooth communication (only applicable for the SPIKE). 

[Download LabView here.](https://www.ni.com/en-us/support/downloads/software-products/download.labview.html#369643) 

You can [download the IDE from this repository here](https://github.com/chrisbuerginrogers/ME35_21), and it is compatible with any version of LabView, including the Community Version.

### ESP8266 Wifi Dongle 
The ESP8266 is a microcontroller that is a cost-effective and highly integrated Wi-Fi MCU for IoT applications. Since the Lego SPIKE Prime kit does not come with WiFi capabilities, the ESP8266 was created as a "backpack" for the SPIKE Prime. A cable was soldered to the TX, RX, Ground, and VCC pins of the ESP and can be connected to the respective RX, TX, Ground, and VCC pins of the SPIKE Prime through one of the ports. This allows the SPIKE and ESP to communicate via UART serial communication. Micropython was flashed onto the ESP and there are two versions of the dongle based on what type of communcation is used (API calls vs. MQTT).
#### Setting Up ESP8266 for API Call Capabilities 
Please follow **all** [instructions on this website](https://quickest-palladium-2e9.notion.site/ESP8266-505d37c06286455887f8698031602e19) for setup. The files referenced are located in the ESP8266 folder on this repository.
#### Setting Up ESP8266 for MQTT Capabilities
Please follow **up to step "III. Install the MicroPython firmware onto the ESP8266"** on [this website](https://quickest-palladium-2e9.notion.site/ESP8266-505d37c06286455887f8698031602e19). Then follow instructions listed in the ESP8266 folder on this repository.

### ThingWorx 
[Follow this PDF](https://drive.google.com/file/d/1n7FzggdS_vQJa6Vi_tX7A-PuhZwObpXY/view?usp=sharing) to create an API Key.

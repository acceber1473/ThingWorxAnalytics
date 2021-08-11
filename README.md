# Integrating SPIKE Prime Robotics with ThingWorx Analytics 
An exploration into the capabilities of PTC's IoT platform ThingWorx, specifically its Analytics Builder and server, and possible applications using Lego SPIKE Prime Robotics.
# Table of Contents
1. [Overview](#Overview)
2. [Setup](#Setup)
3. [Equipment](#Equipment)

## Overview 

<img align="right" src="https://user-images.githubusercontent.com/49819466/128409745-270eaaea-e580-485b-9fd5-d6a1e227b1f7.jpg" width=50% height=50%>

This repository contains ThingWorx and Lego SPIKE Prime code that allows the SPIKE to be trained using the analytics server extension on ThingWorx. 

This project is played an important role in my overall goal of this summer: explore machine learning methods integrable with Lego SPIKE Prime robotics to create an educational AI experience for students. 

A simple ball launcher was built and trained using linear regression to better understand how to integrate ThingWorx with SPIKE Prime. Then, more complex methods of training (eg. neural networks, gradient boosts, random forests, etc.) were explored using the SPIKE Prime puppy system, with a MQTT protocol acting as the main communication method between SPIKE and ThingWorx Analytics. 

To the right is a flowchart of the general training process. Although the SPIKE Puppy is featured, the process is applicable to any SPIKE system.

## Setup
Each folder will contain files detailing setups specific to the systems used. [Here](https://drive.google.com/drive/folders/1ASOn0lAOdE_gR4C9Febgn0rY1Nz9imzS?usp=sharing) is a link to a Google Drive with all of the linked resources and more!

## Equipment
- ThingWorx instance with the following:
  - Analytics Server Extension
  - CSV Parser Extension
  - MQTT Extension
- SPIKE Prime Kit 
- ESP8266 wifi dongle 
  - [Click here](https://quickest-palladium-2e9.notion.site/SPIKE-Prime-Backpacks-31f12415b3ad429fba34956b9d50b49e) to get more info
- [MQTTX](https://mqttx.app/)- a cloud based broker app used as a bridge between SPIKE and ThingWorx 
  - I have not explored other MQTT broker software, but hear that [Mosquitto](https://mosquitto.org/) is reputable

# SPIKE Ball Launcher Example 
# Table of Contents
1. [Overview](#Overview)
2. [Setup](#Setup)
3. [Training](#Training)
<img align="right" src="https://user-images.githubusercontent.com/49819466/128962304-5829e956-a106-4cab-8d91-d1343155e485.jpg" width=50% height=50%>

## Overview
The first SPIKE system I build to be trained by ThingWorx was a ball launcher. The ball launcher consisted of an ultrasonic sensor to measure the distance between the system and the cup (the goal), and paired motors that rotated the launcher arm. The goal was to push trial data (RPM of motors and resultant ball distance) to ThingWorx, create a model using the Analytics extension, and then utilize that model in real-time. 

## Setup

## Training
Through my exploration of ThingWorx Analytics, I found two methods of training: using the Analytics Builder UI, and by calling various Analytics Server services.
### Analytics Builder and PMML Models 

### Analytics Server Services 

Training and validation data were pushed up from the SPIKE to ThingWorx and vice versa using Google Colab and serial connection between the computer and the SPIKE. This Colab notebook contains the code for that: [![Link to Colab Notebook](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)

Here is a flow chart detailing 

<img align="right" src="https://user-images.githubusercontent.com/49819466/128961182-ff2b338c-91f3-4e8f-ad84-03285bdb456f.jpg" width=50% height=50%>

Where does the text go

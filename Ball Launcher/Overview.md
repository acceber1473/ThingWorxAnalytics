# SPIKE Ball Launcher Example 
<img align="right" src="https://user-images.githubusercontent.com/49819466/128962304-5829e956-a106-4cab-8d91-d1343155e485.jpg" width=50% height=50%>

# Table of Contents
1. [Overview](#Overview)
2. [Setup](#Setup)
3. [Training](#Training)

## Overview
The first SPIKE system I build to be trained by ThingWorx was a ball launcher. The ball launcher consisted of an ultrasonic sensor to measure the distance between the system and the cup (the goal), and paired motors that rotated the launcher arm. The goal was to push trial data (RPM of motors and resultant ball distance) to ThingWorx, create a model using the Analytics extension, and then utilize that model in real-time. 

## Setup
### Run Google Colab in a Local Runtime 
Jupyter is a free, open-source, interactive web tool known as a computational notebook, which researchers can use to combine software code, computational output, explanatory text and multimedia resources in a single document. Google Colab, is Google's version, which has the benefit of real time colaboration, just like it's other products like Google Docs. Additionally, Google Colab isn't traditionally run on your local machine, it is ran over the cloud using one of Google's computers.This has it's drawbacks, most notably that since it is hosted on another machine, you can't communicate to local devices. (ex. A microcontroller through serial communication). To solve this we change the connection from a hosted runtime, to a local runtime. However, there a few things we need to install first.
#### Installation
Python: [download from their website](https://www.python.org/downloads/v)
-If you see options to Add to Path or Install pip select them, they are important
Install Jupyter notebook, this can and should be done from the command line using pip or pip3
```bash
  pip install notebook
```
(Optional) You can open Jupyter Notebook as 
```bash
  jupyter notebook
```
Install Google's Library for Communication
```bash
  pip install jupyter_http_over_ws
  jupyter serverextension enable --py jupyter_http_over_ws
```
#### Setup
You can start a Jupyter notebook with the following command 
```bash
  jupyter notebook --NotebookApp.allow_origin='https://colab.research.google.com' --port=8888 --NotebookApp.port_retries=0
```
There will be a link in the command line that looks like this...<img width="1017" alt="Screen Shot 2021-08-12 at 11 19 17 AM" src="https://user-images.githubusercontent.com/49819466/129222956-843a797f-13b8-4402-8c87-2f7a59fab503.png">
Copy that link by selecting it in your terminal, you need it for the next step
Now select connect in the upper right hand corner of your google colab page, select connect to local runtime, and paste the link you just copied into the field and press connect. If it was succesful, it will have a green check mark and say Connected (Local). Success!!<img width="639" alt="Screen Shot 2021-08-12 at 11 22 17 AM" src="https://user-images.githubusercontent.com/49819466/129223450-c16cff9e-4d8f-47ba-8542-f8e6ea00943a.png">

## Training
Through my exploration of ThingWorx Analytics, I found two methods of training: using the Analytics Builder UI, and by calling various Analytics Server services.
### Analytics Builder and PMML Models 

### Analytics Server Services 

Training and validation data were pushed up from the SPIKE to ThingWorx and vice versa using Google Colab and serial connection between the computer and the SPIKE. This Colab notebook contains the code for that: [![Link to Colab Notebook](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)

Here is a flow chart detailing 

<img align="right" src="https://user-images.githubusercontent.com/49819466/128961182-ff2b338c-91f3-4e8f-ad84-03285bdb456f.jpg" width=50% height=50%>

Where does the text go

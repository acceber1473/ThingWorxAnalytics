# SPIKE Ball Launcher Example 
<img align="right" src="https://user-images.githubusercontent.com/49819466/128962304-5829e956-a106-4cab-8d91-d1343155e485.jpg" width=50% height=50%>

# Table of Contents
1. [Overview](#Overview)
2. [Setup](#Setup)
3. [Training](#Training)
4. [Demo](#Demo) 

## Overview
The first SPIKE system built to be trained by ThingWorx was a ball launcher. The ball launcher consisted of an ultrasonic sensor to measure the distance between the system and the cup (the goal), and paired motors that rotated the launcher arm. The goal was to push trial data (RPM of motors and resultant ball distance) to ThingWorx, create a model using the Analytics extension, and then utilize that model in real-time. 

This repository cover two methods of training: using the Analytics Builder in ThingWorx and implementing the resultant PMML predictive model, and solely using Analytics Server Services.

**Method 1** creates a CSV file on Colab with the data read from the SPIKE, imports the CSV File into the Analytics Builder, and then exports the resultant predictive PMML model to be imported back into Colab. 

**Method 2** pushes SPIKE data from Colab into ThingWorx via API Call, where already defined services can be called to do all the predicting. 

## Setup
### Run Google Colab in a Local Runtime (both methods)
Jupyter is a free, open-source, interactive web tool known as a computational notebook, which researchers can use to combine software code, computational output, explanatory text and multimedia resources in a single document. Google Colab, is Google's version, which has the benefit of real time colaboration, just like it's other products like Google Docs. Additionally, Google Colab isn't traditionally run on your local machine, it is ran over the cloud using one of Google's computers.This has it's drawbacks, most notably that since it is hosted on another machine, you can't communicate to local devices. (ex. A microcontroller through serial communication). To solve this we change the connection from a hosted runtime, to a local runtime. However, there a few things we need to install first.
#### Installation
- Python: [download from their website](https://www.python.org/downloads/v)
  - If you see options to Add to Path or Install pip select them, they are important
- Install Jupyter notebook, this can and should be done from the command line using pip or pip3
```bash
  pip install notebook
```
(Optional) You can open Jupyter Notebook as 
```bash
  jupyter notebook
```
- Install Google's Library for Communication
```bash
  pip install jupyter_http_over_ws
  jupyter serverextension enable --py jupyter_http_over_ws
```
#### Setup
You can start a Jupyter notebook with the following command 
```bash
  jupyter notebook --NotebookApp.allow_origin='https://colab.research.google.com' --port=8888 --NotebookApp.port_retries=0
```
There will be a link in the command line that looks like this...
<img width="900" alt="Screen Shot 2021-08-12 at 11 19 17 AM" src="https://user-images.githubusercontent.com/49819466/129222956-843a797f-13b8-4402-8c87-2f7a59fab503.png">

Copy that link by selecting it in your terminal, you need it for the next step
Now select connect in the upper right hand corner of your google colab page, select connect to local runtime, and paste the link you just copied into the field and press connect. If it was succesful, it will have a green check mark and say Connected (Local). Success!!
<img align="center" src="https://user-images.githubusercontent.com/49819466/129223450-c16cff9e-4d8f-47ba-8542-f8e6ea00943a.png" width='639'>

### Creating a ThingWorx Thing (Method 2)
Click here for a video overview on the Ball Launcher Thing created in the ThingWorx Composer. 

### PyPMML Module for Predictive Model Implementation (Method 2)
This portion of the setup is only applicable if you want to manually export the PMML XML predictive model file from ThingWorx. [All credits go to this repository.](https://github.com/autodeployai/pypmml)
- Installation
```bash
  pip install pypmml
```
OR
```bash
  pip install --upgrade git+https://github.com/autodeployai/pypmml.git
```
- Usage
  - Load a model (in this case it would be the local file exported from ThingWorx)
  ```bash
    from pypmml import Model
    # The model is from http://dmg.org/pmml/pmml_examples/KNIME_PMML_4.1_Examples/single_iris_dectree.xml
    model = Model.load('single_iris_dectree.xml')
  ```
  - Call predict(data) to predict new values
  ```bash
    model.predict({'sepal_length': 5.1, 'sepal_width': 3.5, 'petal_length': 1.4, 'petal_width': 0.2})
    {'probability_Iris-setosa': 1.0, 'probability_Iris-versicolor': 0.0, 'probability': 1.0, 'predicted_class': 'Iris-setosa', 'probability_Iris-virginica': 0.0,       'node_id': '1'}
  ```
## Training
Through my exploration of ThingWorx Analytics, I found two methods of training: using the Analytics Builder UI, and by calling various Analytics Server services.
### Method 1: Analytics Builder and PMML Models 
<img align="right" src="https://user-images.githubusercontent.com/49819466/128961182-ff2b338c-91f3-4e8f-ad84-03285bdb456f.jpg" width=50% height=50%>

[ThingWorx Analytics Builder](https://support.ptc.com/help/thingworx/analytics/r9/en/#page/analytics%2Fanalytics_builder%2Fanalytics_builder_overview.html%23) extends ThingWorx Foundation functionality with access to analytic capabilities, including predictive model building, predictive scoring, and data analysis. On ThingWorx, you can manually import a CSV file with all the data and then select the preferred specifications in the builder UI. Then, the resulting PMML model can be exported and imported into Google Colab using a Python pypmml module. 
A PMML (Predictive Model Markup Language) model is an XML-based standard used to represent predictive models. The [pypmml module](https://github.com/autodeployai/pypmml) is a Python PMML scoring library that allows you to import a PMML XML file locally from your computer, and then you can utilize various functions, such as the predict function to ouput motor RPM based on the distance input.
[This PDF](https://drive.google.com/file/d/1Byz2DXAMCUHk4aAdHHu31jjbLcdRjuoJ/view?usp=sharing) is an overview of the training process using the Builder and then exporting/implementing the predictive PMML Model. 
This video goes over using the Analytics Builder to create and export a predictive model.

### Method 2: Analytics Server Services 
The other way to train data solely relies on calling the ThingWorx Analytics Server Extension Services, bypassing the need to manually import and export data/files from the Analytics Builder UI. Here is a Google Colab notebook that details all the API calls used to push data and call services: 

[![Link to Colab Notebook](< img src = "https://colab.research.google.com/assets/colab-badge.svg" height = "10" />)](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)

## Demo
https://user-images.githubusercontent.com/49819466/129241912-d01b0260-5cb5-4e8c-a65c-db4f71e16bab.mp4

[Link](https://drive.google.com/file/d/12A6mukXxOnVAIGvi36IIqErGakunG7yH/view?usp=sharing) to a better resolution version of the video.


# Overview of ThingWorx Services 
![services_flowchart](https://user-images.githubusercontent.com/49819466/128407966-ecd0203b-5cc9-4526-a695-d3d93114c313.jpg)

There are four main services I created to use when generating predictive models using the Analytics server on ThingWorx: refresh, createAnalyticsDataset, trainModel, and predictiveScoring.

## Where I Get Data and How I Store It 
I have mainly been working with Lego's SPIKE Prime kit, and push data from the SPIKE up to ThingWorx through both API calls and a MQTT protocol. Either way, I store data in a value stream through creating data properties that are marked "persistent" and "logged". Then I run the value stream through several services to create a model. 

## 4 Main Services 

### 1. Refresh
Every time I want to create a new model, I purge all my properties and reset them to values that will allow future property values to be stored in value streams properly. I call on the generic "purge all property history" service and then set whatever properties I have accordingly. I can check the status of my data by running the "createInfoTablefromVS" service, which allows me to view all the value stream data in an infotable. 

### 2. createAnalyticsDataset
After I have pushed up all the data I want to consider for the predicitive model to ThingWorx, I then use the CSV Parser Extension to convert the value stream data into a CSV File, JSON metadata file, and an overall dataset. The code takes the CSV and JSON files and stores them in the ThingWorx File Repository, and with the appropriate tags and types of data, these datasets can appear in the Analytics Builder UI as well. The dataset is created with reference to an analytics dataset data shape that is already provided by ThingWorx. The output of this service will be a dataset URI and you can check the status of this job by going into your instance's Analytics Server Data Thing and running the getJobStatus() service. 

### 3. trainModel 
After the dataset URI is generated, this service can create an analytical model based on several inputs. The Analytics Server Training Thing's createJob() service is used and you are able to adjust specifications like the types of machina learning learners you want used for your model. This service will output the modelURI. You can check the status of this by going into the Analytics Server Training Thing and running the getJobStatus() service. 

### 4. predictiveScoring
After creating a predictive model, you can use predictive or prescriptive scoring in order to utilize that model. I wanted to use the analytics model to generate outputs based on specific inputs and called on the Analytics Server Prediction Thing's RealtimeScore() service to do so. For this service, the code creates an infotable with the current property values that will serve as the inputs, and then generates one output for your goal property. At the moment, ThingWorx only supports one goal variable. 

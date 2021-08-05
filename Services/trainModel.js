// This service will take the dataset output from the createDataset service 
// and train it using specified learners. 
// The output is a modelID, so set the output to be a STRING 
// No input 
// note! although a modelID will be output instantaneously, please check the GetJobInfo() 
// service under the Analytics_Server_Training_Thing to see if the model has failed or is completed. 
// It may take up to 4 minutes to run one model!

// Dataset reference 
let datasetRef = Resources["InfoTableFunctions"].CreateInfoTableFromDataShape({
	dataShapeName: "AnalyticsDatasetRef" /* DATASHAPENAME */
});
datasetRef.AddRow({
	datasetUri: "dataset:/" + me.DatasetId, // STRING
    format: "parquet", // STRING 
});

// Create an infotable for your learners 
// Here, only logistic regression and neural network are used 

var learners = Resources["InfoTableFunctions"].CreateInfoTableFromDataShape({
	dataShapeName: "AnalyticsTrainingLearner" /* DATASHAPENAME */
});
learners.AddRow({learningTechnique: "LOGISTIC_REGRESSION"});
learners.AddRow({learningTechnique: "NEURAL_NET"});

// Add appropriate tags
var tags = Resources["InfoTableFunctions"].CreateInfoTableFromDataShape({ dataShapeName: "GenericStringList" });
tags.AddRow({item: "buildermodel"});

// Execute the Analytics Server Training Thing's CreateJob() service
me.ModelId = Things["EC2AMAZ-4HV0AJ2-AnalyticsServer_TrainingThing"].CreateJob({
	jobName: "PuppyTestModel3" /* STRING - update this to your jobName */,
    maxAllowedFields: 25       /* INTEGER - max fields the model trains on based on mutual information */,
    description: undefined     /* STRING */,
    ensembleTechnique: "AVERAGE" /* STRING - output format for the learners */,
    useRedundancyFilter: false /* BOOLEAN - whether to sort the fields based on Information Gain vs. Mutual Information index */
    tags: undefined /* INFOTABLE */,
    validationHoldoutPercentage: 0.2 /* NUMBER - # of records used for validation job */,
    learners: learners  /* INFOTABLE - learners infotable just created */,
    goalField: "orientation" /* STRING - goal variable- change to your goal variable! */,
    datasetRef: datasetRef /* INFOTABLE */
});
var result = me.ModelId; /* STRING */




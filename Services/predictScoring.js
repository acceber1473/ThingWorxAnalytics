// output: Goal Variable (in this case motorRPM) /* STRING */
// This model will apply predictive scoring based off of the modelID generated from the trainModel service.
// First an infotable of the current property values are created, and the RealtimeScore service is then applied, outputting your goal scores!

// create (EMPTY) Infotable containing the features (properties) used for prediction
var modelFeatures = Resources["InfoTableFunctions"].CreateInfoTable({
                infoTableName: "modelFeatures" /* STRING */
});

// create the fields with the corresponding feature (property) name and description
modelFeatures.AddField({name:"name", baseType:"STRING"});
modelFeatures.AddField({name:"description", baseType:"STRING"});

// add a row for each feature (property)
modelFeatures.AddRow({name:"red", description:""});  // replace this with your features
modelFeatures.AddRow({name:"green", description:""});
modelFeatures.AddRow({name:"blue", description:""});
modelFeatures.AddRow({name:"distance", description:""});

// datasetref InfoTable contains features/properties with their current values 
// based on these values the prediction will be executed
var datasetref = Resources["InfoTableFunctions"].CreateInfoTableFromDataShape({
                infoTableName: "datasetref" /* STRING */,
                dataShapeName: "AnalyticsDatasetRef" /* DATASHAPENAME */
});

// get all the property values from the properties specified in the modelFeatures Infotable
var data = me.GetNamedPropertyValues({
                propertyNames: modelFeatures /* INFOTABLE */
});
//var result = data;
// write the properties with their values in the datasetref Infotable
datasetref.AddRow({data:data});

// execute the prediction with the AnalyticsServer_PredictionThing RealtimeScore service
//predictiveScores: INFOTABLE; dataShape: "AnalyticsPredictionScores"

// if you trained through the trainModel service, replace ModelJobID with me.ModelId
var result =  Things["EC2AMAZ-4HV0AJ2-AnalyticsServer_PredictionThing"].RealtimeScore({
	goalField: "orientation" /* STRING */, 
	//modelUri: "results:/models/" + ModelJobID /* STRING */, 
    modelUri: "results:/models/" + me.ModelId /* STRING */,
	datasetRef: datasetref /* INFOTABLE */,
});






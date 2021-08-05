// ThingWorx Service that will create an analytics dataset 
// Takes in a value stream, converts and stores that in a csv file before creating an analytics dataset. 
// Returns a datasetURI- make sure output is set to a STRING

// Create a data infotable calling valuestream's QueryPropertyHistory service 
// Make sure properties of interet are marked logged and persistent 
data=me.QueryPropertyHistory({
	maxItems: undefined /* NUMBER */,
	startDate: undefined /* DATETIME */,
	endDate: undefined /* DATETIME */,
	oldestFirst: true /* BOOLEAN */,
	query: undefined /* QUERY */
});
// Remove the timestamp column so we are left with only variable data 
data.RemoveField("timestamp");

// can uncomment to debug but make sure you assign variable "result" only once 
// if debugging, make sure output is set to "INFOTABLE" 
// var result = data;

// Declaring parameters to write a CSV file 
let params = {
	path: me.csvFileName, /* STRING */
    data: data, /* INFOTABLE */
    fileRepository: "PuppyFR",  /* THINGNAME */
    withHeader: true /* BOOLEAN */
};


// Calls the CSV Parser extension to write a CSV file to the file repository 
Resources["CSVParserFunctions"].WriteCSVFile(params);

let datasetRef = Resources["InfoTableFunctions"].CreateInfoTableFromDataShape({
	dataShapeName: "AnalyticsDatasetRef" /* DATASHAPENAME */
});
var entry = new Object();
entry.datasetUri = encodeURI("thingworx://" + "PuppyFR" + me.csvFileName); // if your Thing does not have a property for csvFileName
									   // insert a string with format '/yourCSVFileName.csv' here
								           // insert your File Repository in place of "PuppyFR"
									   // the dataset you create here will be visible in that FR
entry.format = "csv";
datasetRef.AddRow(entry);

// ThingWorx will automatically detect and save the metadata based on the the CSV file just created
let metadata = Things["EC2AMAZ-4HV0AJ2-AnalyticsServer_DataThing"].DetectMetadataJSON({
	datasetRef: datasetRef /* INFOTABLE */
});
// If any changes to the metadata need to be made, they can be done using the code below
// Here the "identifier" field is being modified to be "INFORMATIONAL"
metadata = JSON.parse(metadata);
for (var i = 0; i < metadata.length; i++) {
	if (metadata[i].fieldName == "identifier") {
    	metadata[i].opType = "INFORMATIONAL";
    }
}
// Again, replace "PuppyFR" with your FR name 
Things["PuppyFR"].SaveText({
	path: me.jsonMetaData,  // if you do not have a property for jsonMetaData, or the json file name, replace
			        // format: '/metadata.json'
    content: metadata
});

// Now that you have both the csv and json metadata files, the dataset can be created 
// Here, the dataset can be tagged 
var tags = Resources["InfoTableFunctions"].CreateInfoTableFromDataShape({
	dataShapeName: "GenericStringList" /* DATASHAPENAME */
});
tags.AddRow({ item: "builderdataset" });
tags.AddRow({ item: "builderdatasetname:" + (me.dataSetName).toLowerCase() }); // replace me.dataSetName with "datasetname of your choice"

// The CreateDataset service from the Analytics Server Data Thing is now called 
// Again, replace "PuppyFR", me.jsonMetaData, and me.csvFileName with your 
// file repository name, metadata file name, and csv file name respectively
me.DatasetId = Things["EC2AMAZ-4HV0AJ2-AnalyticsServer_DataThing"].CreateDataset({
	csvHasHeaders: true,
    metadataFileURI: encodeURI("thingworx://" + "PuppyFR" + me.jsonMetaData),
    csvURI: encodeURI("thingworx://" + "PuppyFR" + me.csvFileName),
    tags: tags
});

var result = me.DatasetId; // returns your data set ID
			   // for my Thing, there is a property that will be updated 






// ThingWorx service that will create an infotable by querying property history
// Make sure the properties of intereste are marked logged and persistent 
// No input
// Output must be set to INFOTABLE

data=me.QueryPropertyHistory({
	maxItems: undefined /* NUMBER */, 
	startDate: undefined /* DATETIME */,
	endDate: undefined /* DATETIME */,
	oldestFirst: true /* BOOLEAN */, 
    query: undefined /* QUERY */, 
});
data.RemoveField("timestamp"); // remove timestamp column to just get data
var result = data; // result is INFOTABLE
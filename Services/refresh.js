// This service just resets property values to 0 or None, and then purges all property history. 
// Intended to be used before the start of each new model creation. 
// Also combats value stream issues (blank cells,etc.)
me.xVal = 0;
me.yVal = 0;
me.zVal = 0;
me.red = 0;
me.green = 0;
me.blue = 0;
me.orientation = "none";
me.distance = 0;

// purgeAllPropertyHistory will purge properties within a specific time period
me.PurgeAllPropertyHistory({ 
	endDate: "2021-07-31" /* DATETIME */,
	startDate: "2021-07-01" /* DATETIME */
});
var result = "refreshed!"; 




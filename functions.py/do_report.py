def doReport(dataSource):
	#fetch and prepare data
	data = fetchData(dataSource)
	parsedData=parseData(data)
	filteredData=filterData(parsedData)
	polishedData=polishData(filteredData)

	#run algorithms
	finalData=analyse(polishedData)

	#create and return Report
	report=Report(finalData)
	return report
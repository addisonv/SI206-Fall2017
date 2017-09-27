import csv

output = []
filename = "P1DataA.CSV"
fileOpen = open("P1DataA.csv")
fileReader = csv.DictReader(fileOpen)
for row in fileReader:
	output.append(row)
#for date in output:
	#dob = date["DOB"]
	#dobSpaces = dob.replace("/", " ")
	#dobSplit = dob.split()
	#if dobSplit[1] not in commonDays:
		#commonDays[dobSplit[1]] = 1
	#else:
	#	commonDays[dobSplit[1]] += 1 
keys = output[0].keys()
output = []
for key in keys:
	output.append(key)
print(output)
#output = sorted(commonDays.items(), key=lambda x: x[1])
#print (output[0][0])

#for field in allRows[0]:
#	fields.append(field)
#dataRows = allRows[1:]
#or info in dataRows: 


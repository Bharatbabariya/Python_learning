# csv to json
import csv,json
csvFilePath="F:///Learning/PySpark_learning/Python_learning/Harshit_Vashisth_Python/csv_to_json/2015.csv"
jsonFilePath="F:///Learning/PySpark_learning/Python_learning/Harshit_Vashisth_Python/csv_to_json/csv_to_json.json"

# # read csv file and add to data 
# data={}

# with open(csvFilePath,'r') as csvFile:
#     csvReader = csv.DictReader(csvFile,fieldsname)

# # create new json file and write data into it

# with open(jsonFilePath,'w') as jsonFile:
#     # make it more readable and pretty
#     out = json.dumps( [ row for row in csvReader ] )
#     jsonFilePath.write(json.dumps(data,indent=4))
#     jsonfile.write(out)


import csv
import json

csvfile = open(csvFilePath, 'r')
jsonfile = open(jsonFilePath, 'w')

fieldnames="Country","Region","Happiness Rank","Happiness Score","Standard Error","Economy (GDP per Capita)","Family","Health (Life Expectancy)","Freedom","Trust (Government Corruption)","Generosity","Dystopia Residual"
reader = csv.DictReader( csvfile, fieldnames)
out = json.dumps( [ row for row in reader ] )
jsonfile.write(out)
import csv, json, sys
#if you are not using utf-8 files, remove the next line
#sys.setdefaultencoding("UTF-8") #set the encode to utf8

#check if you pass the input file and output file

# if sys.argv[1] is not None and sys.argv[2] is not None:
#     fileInput = sys.argv[1]
#     fileOutput = sys.argv[2]

Input_jsonFile="F:///Learning/PySpark_learning/Python_learning/Harshit_Vashisth_Python/csv_to_json/csv_to_json.json"
output_csvFile="F:///Learning/PySpark_learning/Python_learning/Harshit_Vashisth_Python/csv_to_json/2015_json_to_csv.csv"

# with open(Input_jsonFile,'r') as JsonFile:
#     csvReader = csv.DictReader(JsonFile)

# with open(output_csvFile,'w') as csvFile:
#     # make it more readable and pretty

inputFile = open(Input_jsonFile) #open json file
outputFile = open(output_csvFile, 'w') #load csv file
data = json.load(inputFile) #load json content
inputFile.close() #close the input file
output = csv.writer(outputFile) #create a csv.write
#output.writerow(data[0].keys())  # header row
for row in data:
    output.writerow(row.values()) #values rowpython
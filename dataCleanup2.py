
#Read a bunch of CSVs and to fetch data from over marked as "0"

#import OS module for accessing files, json module for reading JSON data
import os
import json

#Point out to the folder where json files are placed
directory = os.fsencode("D:\Work\Coding Workshop\Python\T20WC2021_Analysis\Input\Sub\Actual Data File\\")

#Open final output file in write mode
opFile = open("D:\Work\Coding Workshop\Python\T20WC2021_Analysis\\final.txt", "w")

finalDict = {}

#loop through each json file in the folder
for file in os.listdir(directory):

    fileName = os.fsdecode(file)

    filePath = "D:\Work\Coding Workshop\Python\T20WC2021_Analysis\Input\Sub\Actual Data File\\" + fileName

    #Open the file in Read mode
    with open(filePath, "r") as f:
        dataSource = f.read()

        data = json.loads(dataSource)

        #Loop twice to fetch first over information from both innings
        for i in (0,1):
        
            firstOverJSON = data['innings'][i]['overs'][0]
            
            #Fetch values and append to dictionary
            for batsman in firstOverJSON['deliveries']:
                writeValueA = batsman['batter']
                writeValueB = str(batsman['runs']['batter'])

                if writeValueA in finalDict:
                    finalDict[writeValueA] = str(finalDict[writeValueA] )+ "," + str(writeValueB)
                else:
                    finalDict[writeValueA] = str(writeValueB)               

for key in finalDict:
    value = str(key) + ":" + str(finalDict[key]) + ";"
    opFile.write(value)

opFile.close

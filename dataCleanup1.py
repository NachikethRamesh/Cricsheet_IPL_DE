#Read a bunch of CSVs and determine the right files that are needed for this analysis

#import OS module for accessing files, json module for reading JSON data, shutil module for copying files to new folder
import os
import json
from shutil import copyfile

directory = os.fsencode("D:\Work\Coding Workshop\Python\T20WC2021_Analysis\Input\Sub\\")

#loop through every file, if the file is a json file then open it in read only mode and check if the event is "ICC Men's T20 World Cup"
for file in os.listdir(directory):
    fileName = os.fsdecode(file)

    if fileName.endswith(".json"):

        filePath = "D:\Work\Coding Workshop\Python\T20WC2021_Analysis\Input\Sub\\" + fileName

        # print(filePath)

        with open(filePath, "r") as f:
            dataSource = f.read()
            
            data = json.loads(dataSource)
            
            #If event is "ICC Men's T20 World Cup", then copy the file to new folder
            if data['info']['event']['name'] == "ICC Men's T20 World Cup":
                copyfile(os.fsdecode(filePath), os.fsencode("D:\Work\Coding Workshop\Python\T20WC2021_Analysis\Input\Sub\Actual Data File\\" + fileName))



# lab7.4.readDict.py
# This program will read a dict obj from a file 
# Author: Hewa Orang

import json
FILENAME ="testdict.json"

def readDict():

    with open(FILENAME) as f:
        return json.load(f)
    
somedict = readDict()
print(somedict)

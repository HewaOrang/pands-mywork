# lab7.3.dict.py
# This program will store a simple dict to afile as JSON
# Author: Hewa Orang

import json

FILENAME="testdict.json"
sample= dict(name='fred', age=31, grades=[1,34,551])

def writeDict(obj):
    with open(FILENAME, 'wt') as f:
        json.dump(obj,f)

writeDict(sample)
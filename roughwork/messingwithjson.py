# messing with JSON
# This program to demonstrate storing data in json format
# Author: Hewa Orang

import json


electricBill = {
    'name' : 'Andrew',
    'amount' : '99999'
}

with open("storeData.json", "wt") as f:
    json.dump(electricBill, f) # writes the dictionary object to the file as a JSON object




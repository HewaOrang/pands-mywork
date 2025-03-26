# lab6.7.doView.py
#This program show doView function
#Author: Hewa Orang


def displayModules(modules):
    print ("\tName  \tGrade")
    for module in modules:
        print(f"\t{module['name']}     \t{  module['grade']}")

def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"]);


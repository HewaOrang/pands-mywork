#lab6.5.readIn.py
#This reads in modules
#Author: Hewa Orang

def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit):")

    while moduleName != "":
        module = {}
        module["name"]= moduleName
        module["grade"]= int(input("\t\tEnter grade:"))
        modules.append(module)
        moduleName = input("\tEnter next Module name (blank to quit):")

    return modules

students=[]

def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("enter name :")
    currentStudent["modules"] = readModules()

    students.append(currentStudent)

doAdd(students)
doAdd(students)

print(students)









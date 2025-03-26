#lab6.4.doAdd.py
#This reads in student
#Author: Hewa Orang

students=[]

def readModules():
    return []

def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("enter name :")
    currentStudent["modules"] = readModules()

    students.append(currentStudent)

doAdd(students)
doAdd(students)

print(students)

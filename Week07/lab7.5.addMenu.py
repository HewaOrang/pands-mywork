#lab7.6.addMenu.py
#This program addes DoSave function
#Author: Hewa Orang

students= []

def displayMenu():
    print("What would you like to do?")
    print("t(a) Add new student")
    print("t(v) View students")
    print("t(s) save students")
    print("t(q) Quit")
    choice =  input("Type one letter (a/v/q):").strip()

    return choice

def doAdd(students):
    print("in adding")

def doView(students):
    print("in viewing")

def doSave(students):
    print("in save")

# main program

choice = displayMenu
while(choice != 'q'):
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice == 's':
        doSave(students)    
    elif choice !='q':
        print("\n\nplease select either a,v or q")
    choice=displayMenu()

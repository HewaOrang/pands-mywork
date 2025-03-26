# lab6.3.smpApp.py
# This program propmts the user to keeps displaying the menu in smp.py until q is picked.
# Author: Hewa Orang

def displayMenu():
    print("What would you like to do?")
    print("t(a) Add new student")
    print("t(v) View students")
    print("t(q) Quit")
    choice =  input("Type one letter (a/v/q):").strip()
    return choice
def doAdd():
    # we fill this later
    print("in adding")
def doView():
    # we fill this la
    print("in viewing")

# main program
choice = displayMenu
while(choice != 'q'):
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice !='q':
        print("\n\nplease select either a,v or q")
    choice=displayMenu()

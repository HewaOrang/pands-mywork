# lab7.2.init.py
# This program initializes a file and adds to it
# Author: Hewa Orang



import os.path
FILENAME = "count.txt"
if not os.path.isfile (FILENAME):
    print ("file does not exist")
    writeNumber(0)


def readNumebr():
    try:
        with open(FILENAME) as f:
            number = int(f.read())
            return number
    except IOError:

        return 0

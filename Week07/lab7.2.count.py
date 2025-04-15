# lab7.2.count.py
# This program counts how many time it was run.
# Author: Hewa Orang


FILENAME = "count.txt"

def readNumber():
    with open(FILENAME) as f:
        number = int(f.read())
        return number
# test it
#num = readNumber()
#print (num)

def writeNumber(number):
    with open(FILENAME, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number))

# test it
#writeNumber(6)

# main 
num = readNumber()
num += 1
print (f"we have run this program {num} times")
writeNumber(num)
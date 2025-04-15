# Messing with files
# Author: Hewa Orang

FILENAME = "data.txt"

'''
with open(FILENAME) as f:
   for data in f:
    #print(data , end="")
    print(data.strip())   # This is the prefered way by AB
    #print(data[:-1])
'''
with open("data2.txt", "w+") as f: 
    f.write("what the hell\n")
    f.write("brown cow\n")
    f.seek(0)
    data = f.read()
    print(data)

print("done")


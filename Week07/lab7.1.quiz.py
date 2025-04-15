#lab7.1.quiz.py
#This program answers the quiz of topic 7
#Author: Hewa Orang

# a) Answer give an error as the file doesn't exist

'''
with open("tesst-a.txt") as f:
    data = f.read()
    print (data)

# b) 7 
#   13

with open("test-b.txt", "w") as f:
    data = f.write("test b\n")
    print (data)

with open("test-b.txt", "w") as f2:
    data = f2.write("another line\n")
    print (data)

# c) another line 
'''
with open("test-d.txt", "w") as f:
    data = f.write("test d\n")
    print (data)

with open("test-d.txt", "a") as f2:
    data = f2.write("another line\n")
    print (data)

# d) test d
#    another line


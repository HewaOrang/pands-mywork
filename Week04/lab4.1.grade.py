# lab4.1.grade.py
# This program reads in student's percentage mark and prints the corresponding grade
# Author: Hewa Orang

percentage = float(input("Enter the percentage: "))

if percentage < 0 or percentage > 100:
    print ("Please enter a number between 0 and 100")
elif percentage < 40: 
    print("Fail")
elif percentage < 50:
    print("Pass")
elif percentage < 60:
    print("Merit1")
elif percentage < 70:
    print("Merit2")
else:
    print ("Distinction")

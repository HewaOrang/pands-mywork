# lab3.1.div.py
# This program reads in two numbers and divided the first one by the second and gives the result as intger with the remainder
# Author: Hewa Orang

x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))

answer = int(x/y) 
remainder =x%y 

print(f"{x} divided by {y} is {answer} with remainder {remainder}")

# lab4.2.guess1.py
# This program prompts the user to guess a number, then the program keeps prompting the user until the user gets the right one.
# Author: Hewa Orang

number_to_guess = 30

guess = int(input("Please guess the number:"))
while guess != number_to_guess:
    print ("Wrong")
    guess = int(input("Please guess again:"))

print ("Well done! Yes the number was", number_to_guess)
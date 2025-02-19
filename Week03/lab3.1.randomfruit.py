# lab3.1.randomfruit.py
# This program points out a random fruit
# Author: Hewa Orang

import random

fruits = ['Apple', 'Orange', 'Banana', 'Pear']
index = random.randint(0,len(fruits)-1)

fruit = fruits[index]
print(f"A random Fruit:{fruit}")

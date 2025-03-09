# lab5.3.random.py
# This program puts 10 random numbers into a queue[list], then outputs all the values in the queue, then takes the numbers
# from the queue one at a time, print it and the current number still in the queue.
# Author: Hewa Orang

import random
queue = []
numberofNumbers = 10
rangeTo=100

for n in range (0,numberofNumbers):
    queue.append(random.randint(0, rangeTo))

print (f"queue is {queue}")

while len(queue) != 0:
    currentNumber = queue.pop(0)
    print(f"current Number is {currentNumber} and the queue is {queue}")

print ("the queue is now empty")

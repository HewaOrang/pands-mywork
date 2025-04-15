# lab8.6. his plot.py
# This program makes a hist plot of a random list of salaries
# Author: Hewa Orang

import numpy as np
import matplotlib.pyplot as plt

min_salary = 20000
max_salary = 80000
number_of_entries = 10

np.random.seed(1)

salaries = np.random.randint(min_salary, max_salary, number_of_entries)

plt.hist(salaries)
plt.show()

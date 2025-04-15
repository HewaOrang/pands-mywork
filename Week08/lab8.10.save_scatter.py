# lab8.10.save_scatter.py
# This program makes a hist plot of a random list of salaries
# Author: Hewa Orang

import numpy as np
import matplotlib.pyplot as plt

min_salary = 20000
max_salary = 80000
number_of_entries = 100

np.random.seed(1)

salaries = np.random.randint(min_salary, max_salary, number_of_entries)
ages = np.random.randint(low=21, high = 65, size = number_of_entries)
plt.scatter(ages, salaries, label="salaries")
# plt.show()

xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, color= 'r', label = "x squared")

plt.title("random plot")
plt.xlabel("salaries")
plt.ylabel("age")
plt.legend()
plt.savefig('prettier-plot.png')



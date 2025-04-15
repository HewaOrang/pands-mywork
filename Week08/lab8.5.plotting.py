# lab8.5.plotting.py
# This program plots the function
# Author: Hewa Orang

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints 

plt.plot(xpoints, ypoints)
plt.show()
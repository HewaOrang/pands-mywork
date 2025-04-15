# lab8.11.counties_pie.py
# This program makes a pie plot of list of counties and unique occurances of values in an array.
# Author: Hewa Orang

import numpy as np
import matplotlib.pyplot as plt

possible_counties = ['mayo', 'Galway', 'Roscommon', 'Dublin', 'Donegal']
counties = np.random.choice(
    possible_counties,
    p=[0.1, 0.3, 0.2, 0.12, 0.28 ],
    size=(100)
)

unique, counts = np.unique(counties, return_counts=True)

plt.pie(counts, labels= unique)

plt.show()
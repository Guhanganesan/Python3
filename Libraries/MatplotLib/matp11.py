import numpy as np
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

ages_x=[25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_indexes=np.arange(len(ages_x))

width=0.25

dev_y=[38496, 42000, 46752, 49320, 53200, 56000, 62316, 67317, 68748, 73752, 67895]

dev_z=[39496, 43000, 47752, 50320, 54200, 57000, 63316, 68317, 69748, 75752, 72895]

plt.bar(x_indexes, dev_y, color='g', width=width, label="All Devss")

plt.bar(x_indexes, dev_z, color='r', width=width, label="Python Devs")

plt.title("Median Salary INR by Age")

plt.xlabel("Ages..")

plt.ylabel("Meidan Salary")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.show()


#Style, Grid and Layout and save as image
#Bar 
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

dev_x=[25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y=[38496, 42000, 46752, 49320, 53200, 56000, 62316, 67317, 68748, 73752, 67895]

plt.plot(dev_x, dev_y, color='r', label="All Devss")

plt.bar(dev_x, dev_y, color='g', label="All Devss")

plt.title("Median Salary INR by Age")

plt.xlabel("Ages..")

plt.ylabel("Meidan Salary")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.show()


#Grid and Layout

from matplotlib import pyplot as plt

dev_x=[25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y=[38496, 42000, 46752, 49320, 53200, 56000, 62316, 67317, 68748, 73752, 67895]

py_dev_y=[43800, 44000, 56752, 59320, 59820, 65000, 68316, 72317, 76748, 77752, 78895]

plt.plot(dev_x, dev_y, color='#5a7d9a', linestyle='--', linewidth=3, marker='.', label="All Devs")

plt.plot(dev_x, py_dev_y, color='g', marker='o',  label="Python")

plt.title("Median Salary INR by Age")

plt.xlabel("Ages..")

plt.ylabel("Meidan Salary")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.show()


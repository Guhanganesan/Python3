#Bar chart and Histogram

import matplotlib.pyplot as plt

x1=[2,4,6,8,10]
y1=[6,7,8,2,4]

x2=[1,3,5,9,11]
y2=[7,8,2,4,2]

plt.bar(x1,y1, label="Bars 1")
plt.bar(x2,y2, label="Bars 2")

plt.xlabel("x")
plt.ylabel("y")
plt.title("This is a bar chart")
plt.legend()
plt.show()


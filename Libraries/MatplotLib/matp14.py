#Stack Plot

import matplotlib.pyplot as plt

days=[1,2,3,4,5,6]
eating=[2,3,3,2,4,5]
working=[7,4,6,8,9,5]
playing=[8,7,8,9,6,7]

plt.plot([],[],color='m', label="Sleeping", linewidth=5)
plt.plot([],[],color='c', label="Eating", linewidth=5)
plt.plot([],[],color='r', label="Working", linewidth=5)
plt.plot([],[],color='k', label="Playing", linewidth=5)

plt.stackplot(days,eating,working,playing,colors=['m','c','r','k'])

plt.xlabel("x")
plt.ylabel("y")
plt.title("This is a bar chart")
plt.legend()
plt.show()


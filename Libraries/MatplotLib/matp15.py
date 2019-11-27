#Pie Chart

import matplotlib.pyplot as plt

days=[1,2,3,4,5,6]
eating=[2,3,3,2,4,5]
working=[7,4,6,8,9,5]
playing=[8,7,8,9,6,7]

slices=[7,2,2,13]
activities=["days","eating","working","playing"]
cols=['m','c','r','k']
plt.pie(slices,labels=activities,colors=cols, startangle=80, shadow=True, 
        explode=(0,0.1,0,0))


plt.title("This is a pie chart")

plt.show()


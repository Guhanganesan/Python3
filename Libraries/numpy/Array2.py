#Numerical Ranges and Slicing

import numpy as np 
x = np.arange(5) 
print(x)

x = np.arange(5, dtype = float)
print(x)

x = np.arange(10,20,2) 
print(x)

a = np.arange(10) 
s = slice(2,7,2) 
print(a[s])  #[2 4 6]

a = np.arange(10) 
b = a[2:7] 
print(b)   #[2 3 4 5 6]

a = np.arange(10) 
print(a[2:])    #[2 3 4 5 6 7 8 9]
print(a[:5])    #[0 1 2 3 4]
print(a[-5:-1]) #[5 6 7 8]



















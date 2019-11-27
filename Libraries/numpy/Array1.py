#Array and its methods

import numpy as np 
a = np.array([[1,2,3,7],[4,5,6,8]]) 
print(a.shape)

#(2,4)

a = np.array([[1,2,3],[4,5,6]]) 
a.shape = (3,2) 
print(a)
"""
[[1 2]
 [3 4]
 [5 6]]
 """

a = np.array([[1,2,3],[4,5,6]]) 
b = a.reshape(3,2) 
print(b)

"""
[[1 2]
 [3 4]
 [5 6]]
"""

a = np.arange(24) 
print(a)
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]

a = np.arange(24) 
print(a.ndim)

b = a.reshape(2,4,3)  #3 dimensions
print(b)

x = np.zeros((5,), dtype = np.int) 
print(x) #default dtype is float


x = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])  
print(x)


x = np.ones(5, dtype=int) 
print(x)


x = np.ones([2,2], dtype = int) 
print(x)

#convert list into array
x = [1,2,3] 
a = np.asarray(x) 
print(a)

s = 'Hello World' 
a = np.frombuffer(s, dtype = 'S1') 
print(a)

# use iterator to create ndarray 
list = range(5) 
it = iter(list)
x = np.fromiter(it, dtype = float) 
print(x)








































































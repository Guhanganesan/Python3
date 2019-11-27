import numpy as np

a=np.array([
    [1,2,3],
    [4,5,6]
])
print(a.size)
print(a.shape) #rows,cols
print(a.dtype)
print(a.ndim) #no of rows
print(a.flatten()) #sinlge dimensional array


a=np.arange(12)
print(a)
a=a.reshape(3,4)
print(a)
a=a.reshape(2,2,3)
print(a)







x = np.array([[1, 2], [3, 4], [5, 6]]) 
y = x[[0,1,2], [0,1,0]] #0->[1,2], 1->[3,4], 2->[5,6]
print(y)  #[1 4 5]


















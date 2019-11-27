#Array Matrix

import numpy as np 
a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 
#print(a)
"""
[[1 2 3]
 [3 4 5]
 [4 5 6]]
 """

print(a[...,1]) #2nd column

print(a[1,...]) #2nd row

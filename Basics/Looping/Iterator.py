import itertools
import operator

L=[3,4,6,7]
s=itertools.accumulate(L)
print(list(s)) #[3, 7, 13, 20] 

s=itertools.accumulate(L, operator.mul)
print(list(s)) #[3, 12, 72, 504]



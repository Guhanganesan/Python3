"""
[23,45,67,89] = [89,45,67,23] Swap 1st and last
"""
L = [23,45,67,89]

temp = 0
length = len(L)

temp=L[0]
L[0]=L[length-1]
L[length-1]=temp

print(L)



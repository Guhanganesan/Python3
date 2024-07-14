def increment_items(L, increment):
    i = 0
    while i < len(L):
        L[i] = L[i] + increment
        i = i + 1
 
values = [1, 2, 3]
print(increment_items(values, 2))
print(values)
"""
None
[3, 4, 5]
"""
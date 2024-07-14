"""
Largest number in a list
"""
L=[4,2,3,1,0,6,5,-3]

mind=0
for index in range(0, len(L)):
    if L[index] > mind:
        mind = L[index]

print("Largest: ", mind)
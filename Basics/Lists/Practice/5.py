"""
Largest number in a list ["Apple", "Dinosar", "Ball","Cat"]
"""
L=["Apple", "Dinosar", "Ball","Cat"]

temp=0
check=0
for index in range(0, len(L)):
    length=len(L[index])
    if length > temp:
        temp=length
        check=index
        
print("Largest: ", L[check])
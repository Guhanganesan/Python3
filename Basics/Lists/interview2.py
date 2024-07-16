# Input : [(1,6),(2,4),(9,7),(5,3)]
# Output: [(9,7),(5,3),(1,6),(2,4)]

L=[(1,6),(2,4),(9,7),(5,3)]
temp=0
for i in range(0, len(L)):
    for j in range(0, len(L)):
        if sum(L[i]) > sum(L[j]):
            temp=L[i]
            L[i]=L[j]
            L[j]=temp
print(L)

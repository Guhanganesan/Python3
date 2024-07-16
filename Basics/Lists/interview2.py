# [(1,6),(2,4),(9,7),(5,3)]
# Requirement:: [(9,7),(5,3),(1,6),(2,4)]

temp=0
L=[(1,6),(2,4),(9,7),(5,3)]
res=[]
for i in range(0, len(L)):
    # print(sum(data))
    # if sum(data) > temp:
    #     temp=data
    for j in range(0, len(L)):
        if sum(L[i]) > sum(L[j]):
            temp=L[i]
            L[i]=L[j]
            L[j]=temp
            
print(L)

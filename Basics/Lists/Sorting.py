L=[2,4,1,6,3,0,5,8,7]
length=len(L)
temp=0

for i in range(0, length):
    for j in range(i+1, length):
        if L[i] > L[j]:
             temp=L[i]
             L[i]=L[j]
             L[j]=temp
print(L)


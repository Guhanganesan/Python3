L=[1,1,3,4,2,1,3,5,6,2,1,3]
length=len(L)
i=0
while(i<=length):
    for j in range(i+1, length):
        if L[i] == L[j]:
             L.pop(j)
             i=i-1
             length = length - 1
             break
    i=i+1
print("After removed duplicates: ")
print(L)

L=[5,1,3,6,8,7,2];
temp=0
for i in range(0,len(L)):
    if(L[i]>temp):
        temp=L[i]
        
print(temp)

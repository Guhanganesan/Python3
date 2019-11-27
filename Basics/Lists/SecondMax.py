L=[5,1,3,6,8,7,2]
f=0
s=0
for i in range(0,len(L)):
    if(L[i]>f):
        s=f
        f=L[i]
    elif(L[i]>s):
        s=L[i]
        
print(f,s)

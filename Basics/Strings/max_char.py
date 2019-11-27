x="malayalamvigadan"
length=len(x)-1
acount=0
bcount=2
temp=''
for i in range(0, length):
    for j in range(1, length):
        if x[i]==x[j]:
           acount+=1
           temp=x[j]
           if acount>bcount: #1>2,2>2,3>2
               bcount=acount #3
               temp=x[j]     
    acount=0  

print("Max repated char is: ",temp)
print("And count is :",bcount)


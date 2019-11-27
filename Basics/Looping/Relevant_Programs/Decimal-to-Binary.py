num=11
sum=0 
count=0 
L=[]
x=" "
while num>0:
    rem=num%2
    L.append(rem)
    num=num//2
    count=count+1
    
for i in range(len(L)-1, -1, -1):
    x=x+str(L[i])
print(int(x))

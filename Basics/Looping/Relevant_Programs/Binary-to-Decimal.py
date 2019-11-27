num=1011
sum=0 
count=0 
while num>0:
    rem=num%10
    sum=sum+rem*(2**count)
    num=num//10
    count=count+1
print(sum)

num=int(input("Enter any number"))
sum=0
count=0
while num>0:
    rem =num%10
    sum=sum+rem*(8**count)
    num=num//10
    count=count+1

print("The octal number is: ", sum)


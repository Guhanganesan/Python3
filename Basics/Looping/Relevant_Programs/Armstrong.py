num=int(input("Enter any number"))
sum=0
test=num
while num>0:
    rem =num%10
    sum=sum+rem**3
    num=num//10

if test==sum:
    print("The given number is armstrong", sum)
else:
    print("Not armstrong number ", sum)


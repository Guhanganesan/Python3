num=int(input("Enter any number"))
sum=0
while num>0:
    rem =num%10
    sum=sum*10+rem
    num=num//10
print("The sum of digit is: ", sum)

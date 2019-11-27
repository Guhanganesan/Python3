num=int(input("Enter any number"))
sum=0
test=num
while num>0:
    rem =num%10
    sum=sum*10+rem
    num=num//10

if test==sum:
    print("The given number is palindrome", sum)
else:
    print("Not palindrome number ", sum)
"""
num=12345

       5    = 0*10+5
       54   = 5*10+4
       543  = 54*10+3
"""
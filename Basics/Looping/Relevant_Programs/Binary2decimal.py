num=int(input("Enter any number"))
sum=0
count=0
while num>0:
    rem =num%10
    sum=sum+rem*(2**count)
    num=num//10
    count=count+1

print("The decimal number is: ", sum)

"""
1 -- 1 * 2^0 = 1
0 -- 0 * 2^1 = 0
1 -- 1 * 2^2 = 4
1 -- 1 * 2*3 = 8
     rem * 2 *(count)  =res

     sum=sum+res
"""
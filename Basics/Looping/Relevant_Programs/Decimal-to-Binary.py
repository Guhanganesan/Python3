num=int(input("Enter Number: "))
sum=0 
L=[]
count=0
while num>0:
    rem=num%2
    L.append(rem)
    print(rem*(2**count))
    sum=sum+rem*(2**count)
    num=num//2
    count=count+1

print("Decimal: ", sum)
binary = [ str(num) for num in L]
print("Binary: ", " ".join(binary))

"""
11 => 1011
"""
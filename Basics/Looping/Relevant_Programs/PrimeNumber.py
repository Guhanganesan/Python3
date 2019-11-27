number=int(input("Enter Number"))
check=False
for i in range(2, int(number/2)):
    if number%i==0:
        check=True

if(check==False):
    print("Prime Number")
else:
    print("Not Prime Number")

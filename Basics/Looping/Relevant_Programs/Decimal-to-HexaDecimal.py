num=int(input("Enter any number"))
L=[]
count=0
x=" "
while num>0:
    rem =num%16
    if rem==10:
        rem="A"
    elif rem==11:
        rem="B"
    elif rem==12:
        rem="C"
    elif rem==13:
        rem="D"
    elif rem==14:
        rem="E"
    elif rem==15:
        rem="F"
    L.append(str(rem))
    num=num//16
    count=count+1

for i in range(len(L)-1,-1,-1):
    x=x+L[i]

print("The octal number is: ", x)

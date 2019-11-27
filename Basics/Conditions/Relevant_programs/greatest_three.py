#gretest among three numbers
a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
c=int(input("Enter 3rd Number"))
if a>b:
    if a>c:
        print("a is greater")
    elif c>a:
        print("c is greater")
    else:
        print("a and c are equal")
elif b>a:
    if b>c:
        print("b is greater")
    elif c>b:
        print("c is greater")
    else:
        print("b and c are equal")
else:
    print("a and b are equal")

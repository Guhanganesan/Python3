num=int(input("Enter any number"))
sum=0
count=0
L=[]
x=" "
while num>0:
    rem =num%8
    print(rem)
    L.append(rem)
    num=num//8
    count=count+1

for i in range(len(L)-1,-1,-1):
    k=str(L[i])
    x=x+k

print("The dicimal to octal number is: ", x)

"""
Answer:-
Enter any number2018
2
4
7
3
The dicimal to octal number is:   3742
"""

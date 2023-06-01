# check with index based

x="malayalam"

length=len(x)-1
count=0
check=False

while length>=0:
    if x[length]!=x[count]:
        check=True
        break
    count+=1
    length-=1

if check:
    print("Given String is not Palindrome")
else:
    print("Palindrome")


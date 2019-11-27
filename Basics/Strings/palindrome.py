# check with index based

x="malayalam"

length=len(x)-1
count=0
temp=''

while length>=0:
    if x[length]==x[count]:
        temp=temp+x[count]
        count+=1
        length-=1
    elif x[length]!=x[count]:
        break

if x==temp:
    print("Given String is Palindrome")
else:
    print("Not palindrome")


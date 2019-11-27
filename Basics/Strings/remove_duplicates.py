x="anandham"
s=list(x)
print(s)
length=len(s)
i=0
while(i<=length):
    for j in range(i+1,length):
        if s[i]==s[j]:
           s.pop(j)
           i=i-1
           length=length-1
           break
    i=i+1
print("".join(s)) #list to string  
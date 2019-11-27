x="friend"
s=list(x) # string to char array
print(s)
temp=''
length=len(s)
for i in range(0,length):
    for j in range(0, length):
            if ord(s[i])<ord(s[j]):
                     temp=s[i]
                     s[i]=s[j]
                     s[j]=temp
print(s)


x="he is my dear friend"
s=x.split()
print(s)

temp=''
length=len(s)
for i in range(0,length):
    for j in range(0, length):
            if ord(s[i][0])<ord(s[j][0]):
                     temp=s[i]
                     s[i]=s[j]
                     s[j]=temp
print(s)

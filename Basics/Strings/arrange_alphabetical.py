x="friend"
s=list(x) # string to char array ['f', 'r', 'i', 'e', 'n', 'd']
print(s)
temp=''
length=len(s)
for i in range(0,length):
    for j in range(i+1, length):
            if ord(s[i]) > ord(s[j]):
                     temp=s[i]
                     s[i]=s[j]
                     s[j]=temp

print("".join(s)) #definr


x="he is my dear friend"
s=x.split() # ['he', 'is', 'my', 'dear', 'friend']
print(s)
temp=''
length=len(s)

for i in range(0,length):
    for j in range(i+1, length):
            if ord(s[i][0]) > ord(s[j][0]):
                     temp=s[i]
                     s[i]=s[j]
                     s[j]=temp
print(" ".join(s))

"""
['f', 'r', 'i', 'e', 'n', 'd']
definr
['he', 'is', 'my', 'dear', 'friend']
dear friend he is my
"""
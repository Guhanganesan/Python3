x="he is my dear friend ranjith"
s=x.split()

length=len(s)
temp=""
for i in range(0,length):
    for j in range(0,length):
        if len(s[i])<len(s[j]):
              temp=s[i]
              s[i]=s[j]
              s[j]=temp
            
print(s[length-1])
print(s)
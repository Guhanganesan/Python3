# --------------------------------------- #

x="he is my dear friend ranjith"
s=x.split()
length=len(s)
temp=""
for i in range(0,length):
      if len(s[i])>len(temp):
              temp=s[i]
            
print(temp) 
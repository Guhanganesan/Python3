s="Iterator objects that will be joined together"
s=s.split()

length=len(s)
temp=""
for i in range(0,length):
    for j in range(i+1,length):
        if len(s[i])>len(s[j]):
              temp=s[i]
              s[i]=s[j]
              s[j]=temp
            
print(s) # ['be', 'will', 'that', 'joined', 'objects', 'Iterator', 'together']
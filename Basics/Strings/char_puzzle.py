# if 'ckr' means 'emt'
# whats is 'tek'?
# 'c'+2 => 'e'
# 'k'+2 => 'm'
# 'r'+2 => 't'

x='tek'
s=list(x)
print(s)
temp=0
strng=''
for i in range(0,len(s)):
    if s[i]=='t':
       temp=ord(s[i])+2
       strng=strng+chr(temp)
    elif s[i]=='e':
       temp=ord(s[i])+2
       strng=strng+chr(temp)
    elif s[i]=='k':
       temp=ord(s[i])+2
       strng=strng+chr(temp) 

print(strng)


print(ord('a')) #unicode values , chr to unicode ->97
print(ord('A')) # 65
print(chr(100))
x=chr(ord('a')+1) #unicode to char
print(x)

"""
"KRVB"=>"MTYD"
"GSAK"=>"IUCM"
"""

s=input("Enter String")
temp=""
print(s)

x=ord(s[0])+2
x=chr(x)
temp=temp+x 

x=ord(s[1])+2
x=chr(x)
temp=temp+x 

x=ord(s[2])+2
x=chr(x)
temp=temp+x 

x=ord(s[3])+2
x=chr(x)
temp=temp+x 

print(temp)


for i in range(0,len(s)):
    x=ord(s[i])+2
    x=chr(x)
    temp=temp+x
    
print(temp)






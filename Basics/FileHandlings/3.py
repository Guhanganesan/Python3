#Read the data

f=open("myfile.txt","r")


#r=f.read() #read all 
#print(r)

#for first line

#line=f.readline()
#print(line)

lines=f.readlines()
print(lines[3:6])   # text stored in list
"""
for i in lines:
     print(i)
"""

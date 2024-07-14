#create new text file
#open("D:\\MYFOLDER\\myfile1.txt","w")
f=open("myfile.txt","w")
f.write("Hello")

#print multiple lines

for i in range(1,11):
   f.write("The text line is {} \n".format(i))


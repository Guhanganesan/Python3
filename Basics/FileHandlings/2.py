#Append Data

f=open("myfile.txt","a")
#f.write("The text line is 11")

for i in range(11,21):
    f.write("The text line is {} \n".format(i))


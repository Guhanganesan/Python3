x="He is my dear friend"
count=0
for i in range(0, len(x)):
    if x[i]=='e':
        count+=1
print(count)

x=input("Enter String")
count=0
for i in range(0,len(x)):
    if x[i]=='e' or x[i]=='E':
        count=count+1 

print("Number of \'e\' or \'E\'",count)
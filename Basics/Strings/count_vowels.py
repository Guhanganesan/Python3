x=input("Enter String")
count=[0,0,0,0,0]
for i in range(0,len(x)):
    if x[i]=='e' or x[i]=='E':
        count[0]=count[0]+1 
    elif x[i]=='i' or x[i]=='I':
        count[1]=count[1]+1 
    elif x[i]=='a' or x[i]=='A':
        count[2]=count[2]+1 
    elif x[i]=='o' or x[i]=='O':
        count[3]=count[3]+1 
    elif x[i]=='u' or x[i]=='U':
        count[4]=count[4]+1 
print(count)
print("Number of \'e\' or \'E\'",count[0])
print("Number of \'i\' or \'I\'",count[1])
print("Number of \'a\' or \'A\'",count[2])
print("Number of \'o\' or \'O\'",count[3])
print("Number of \'u\' or \'U\'",count[4])
"""
Enter String Hello my dear friend how are you
Number of 'e' or 'E' 4
Number of 'i' or 'I' 1
Number of 'a' or 'A' 2
Number of 'o' or 'O' 3
Number of 'u' or 'U' 1
"""
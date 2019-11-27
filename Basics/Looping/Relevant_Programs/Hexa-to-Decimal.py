x=input("Enetr Hexa Decimal Number")
L=list(x)
print(L)
sum=0
count=0
for i in range(len(L)-1,-1,-1):
    if(L[i]=="A"):
        L[i]=10
    elif(L[i]=="B"):
        L[i]=11
    elif(L[i]=="C"):
        L[i]=12
    elif(L[i]=="D"):
        L[i]=13
    elif(L[i]=="E"):
        L[i]=14
    elif(L[i]=="F"):
        L[i]=15
    sum=sum+int(L[i])*(16**count)
    count+=1
print("Decimal Number is: ",sum)



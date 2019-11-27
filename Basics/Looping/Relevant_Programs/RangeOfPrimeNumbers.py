start=int(input("Enter Starting Number"))
end=int(input("Enter Ending Range"))
for number in range(start, (end+1)):
    check=False
    for i in range(2, int(number/2)):
        if number%i==0:
            check=True
    if(check==False):
        print(number)


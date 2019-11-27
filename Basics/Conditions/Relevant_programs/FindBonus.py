salary=int(input("Enter Salary"))
if(salary<0 or salary>=20000):
    print("Invalid Salary")
else:
    if(salary>=0 and salary<=5000):
        print("Provide 5% bonus")
    elif(salary>5000 and salary<=10000):
        print("provide 10% bonus")
    elif(salary>10000 and salary<=20000):
        print("Provide 20% bonus")

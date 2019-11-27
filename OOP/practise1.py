class Student: 
    name=""
    rollNo=0
    mark=0
    def __init__(self,x,y,z):
        self.name=x
        self.rollNo=y
        self.mark=z 
        
    def display(self):
        print("Name: ",self.name)
        print("Roll No: ",self.rollNo)
        print("Mark: ", self.mark)
    
jenna=Student("Jenna",1234,67)
john=Student("John",1235,45)
dom=Student("Dom",1236,56)
karthi=Student("Karthikeyan",1237,40)

L=[jenna,john,dom,karthi] #[67,45,56,40]

temp=Student("",0,0)

for i in range(0,len(L)):
    for j in range((i+1),len(L)):
        if L[i].mark<L[j].mark:
            temp=L[j]
            L[j]=L[i]
            L[i]=temp
            

for i in range(0,len(L)):
    #print("Student",L[i].name,"has Rank",(i+1),"and his marks is:",L[i].mark)
    print("Rank: ",(i+1))
    L[i].display()
    
    
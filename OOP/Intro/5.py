class Calc:
    name="Casio"
    def disp(self):
        print(self.name)
    
obj=Calc()
obj.disp()

class Calc: 
    x=0
    y=0
    def test(): 
        #can't call without using 'self'
        print("Hi")
    def add(self,a,b):
        self.x=a
        self.y=b
        print(self.x+self.y)
    def sub(self):
        print(self.x-self.y)
    def mul(self):
        print(self.x*self.y)
obj=Calc()
obj.test()
obj.add(10,20)
obj.sub()
obj.mul()

class Student: 
    name=""
    rollNo=0
    def setName(self,x):
        self.name=x
    def setRoll(self,y):
        self.rollNo=y 
        
    def display(self):
        print(self.name)
        print(self.rollNo)
    
jenna=Student()
jenna.setName("Jenna Reddy")
jenna.setRoll(1234)
jenna.display()

john=Student()
john.setName("John Kennady")
john.setRoll(1235)
john.display()



class Student: 
    name=""
    rollNo=0
    def getDetails(self,x,y):
        self.name=x
        self.rollNo=y 
        
    def display(self):
        print(self.name)
        print(self.rollNo)
    
jenna=Student()
jenna.getDetails("Jenna Reddy",1234)
jenna.display()

john=Student()
john.getDetails("John Kennady",1235)
john.display()




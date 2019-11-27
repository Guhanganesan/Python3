class Rbi:
    def __init__(self):
        print("Hi I am RBI")
    def rate(self):
        pass
    def add(self):
        print("Hi")
    def test(self,a,b):
        self.a=a
        self.b=b 
        return self.a+self.b

obj=Rbi()
c=obj.test(10,90)
print(c)


#Inheritance(Single)

class MyBank(Rbi):

    def __init__(self):
        print("MyBank")
    
obj=MyBank()
c=obj.test(200,300)
print(c)

#Multilevel

class MyBranch(MyBank):
    def __init__(self):
        print("My Branch")
    def add(self):
        print("Hello")

obj=MyBranch()
obj.add()
c=obj.test(50,10)
print(c)

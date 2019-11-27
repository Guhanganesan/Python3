class Student:
    name="" #instance variable
    age=0
    def __init__(self,a,b):
        self.name=a
        self.age=b
    def display(self):
        print(self.name)
        print(self.age)

priya=Student("Mohana Priya",20)
sangavi=Student("Sangavi Bala",21)
priya.display()
sangavi.display()
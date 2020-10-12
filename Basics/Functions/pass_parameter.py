x = 10
y = 20
def add(a,b):
    x = a
    y = b
    print(x+y) #100

add(40,60)
print(x+y) #30

class Test:
    x = 10
    y = 20
    def __init__(self):
        print("Welcome")
    
    def add(self, a, b):
        self.x = a
        self.y = b
        print(self.x + self.y)

    def __str__(self):
        self.x = 300
        self.y = 400
        print(self.x + self.y)

obj = Test()
obj.add(50,70)
obj.__str__()

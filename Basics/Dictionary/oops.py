class Dict:
    def __init__(self):
        self.d={}
    def add(self,x,y):
        self.d.update({x:y})
    
    def remove(self,key):
        self.d.pop(key)
        
    def update(self,key,value):
        self.d[key]=value
        
    def display(self):
        print(self.d)
        
obj = Dict()
for i in range(1,4):
    key=input("Enter Key")
    value=input("Enter value")
    obj.add(key,value)
    
obj.display()
obj.remove('name')
obj.update('age',32)
obj.display()

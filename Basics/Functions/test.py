class Stack:
    def __init__(self):
        self.list=[]
    def add(self,x):
        self.list.append(x)

    def remove(self):
        self.list.pop()

    def disp(self):
        print(self.list)
    def update(self,pos,elem):
        self.list[pos]=elem

obj=Stack()
obj.add(30)
obj.add(40)
obj.add(60)
obj.add(80)

obj.disp()
obj.remove()
obj.disp()
obj.update(2,75)


        
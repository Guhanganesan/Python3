class Stack:
    def __init__(self):
        self.stack=[]
    def add(self,getValue):
        self.stack.append(getValue)

    def remove(self):
        self.stack.pop()

    def getAll(self):
        return self.stack
    def peek(self):
        return self.stack[len(self.stack)-1]

stack = Stack()
stack.add(10)
stack.add(20)
stack.add(30)

data=stack.getAll()
print(data)

stack.remove()


data=stack.getAll()
print(data)

peek=stack.peek()
print(peek)


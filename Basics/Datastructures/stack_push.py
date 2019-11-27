"""
Stack: Last in First Out
"""
class Stack:
    def __init__(self):
        self.stack=[]
    def add(self, getValue):
        if  getValue not in self.stack:
            self.stack.append(getValue)
            return True
        else:
            return False
    def peek(self):
        return self.stack[0]
    def getAll(self):
        return self.stack

stack = Stack()
stack.add(10)
stack.add(20)

data=stack.peek()
all=stack.getAll()
print(all)
print(data)
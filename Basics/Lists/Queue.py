class Queue:
    def __init__(self):
        self.queue=[]

    def push(self,item):
        self.queue.append(item)

    def display(self):
        print(self.queue)

    def remove(self):
        self.queue.pop(0)

    def update(pos,elem):
        self.queue[pos]=elem

    def size(self):
        print(len(self.queue))

obj = Queue()
obj.push(10)
obj.push(20)
obj.push(30)
obj.display()
obj.remove()
obj.display()
obj.size()
obj.update(2,55)
obj.display()

class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[]*self.__max_size
        self.__top=len(self.__elements)-1
        #self.__top=-1 #-1 is the last element in reverse order
    
    def get_max_size(self):
        return self.__max_size
    
    def is_full(self):
       if self.__max_size==len(self.__elements):
            return True
       else:
           return False

    def push(self,data):
        for i in range(0,len(data)):
            self.__elements.append(data[i])

    
    def is_empty(self):
       if []==self.__elements:
           return True
    
    def pop(self):
        length=len(self.__elements)-1
        for i in range(length,-1, -1):
            self.__elements.pop(i)
            
        print("Popped List:",self.__elements)
        #Remove pass and write the logic to pop an element. Pop the element only if stack is not empty. Otherwise, display appropriate message

    def display(self):
        print(self.__elements)
        print("top is:",self.__top)
        #Remove pass and write the logic to display the element(s).
                                              
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        length=len(self.__elements)-1
        index=0
        while(index<=length):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg

stack1=Stack(3)
print(stack1.get_max_size())
print(stack1.is_full())
stack1.push(["A","B","C"])
print(stack1.is_full())
stack1.display()
stack1.pop()
stack1.display()

stack1.push(["A","B","C"])
print(stack1.__str__())

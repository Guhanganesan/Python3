from node import Node

class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    
    def add(self, data):
        new_node=Node(data)
        if(self.__head is None):
            self.__head=self.__tail=new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail=new_node

    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()

    def find_node(self,data):
        temp=self.__head
        while(temp is not None):
            if(temp.get_data()==data):
                return temp
            temp=temp.get_next()
        return None
    
    def insert(self,data,data_before):
        new_node=Node(data)
        if(data_before==None): # Add at 1st location
            new_node.set_next(self.__head) # self.__next = ??
            self.__head=new_node
            if(new_node.get_next()==None): # self.__next = ??
                self.__tail=new_node
        else: # Add after existing node 
            node_before=self.find_node(data_before)
            if(node_before is not None):
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if(new_node.get_next() is None):
                    self.__tail=new_node
            else:
                print(data_before,"is not present in the Linked list")
    
                                              
biscuit_list=LinkedList()
biscuit_list.add("Goodday")
biscuit_list.add("Bourbon")
biscuit_list.add("Hide&Seek")
biscuit_list.add("Nutrichoice")

# biscuit_list.display()

# biscuit_list.find_node("Bourbon")

biscuit_list.insert("5050", None)

biscuit_list.display()

print("=========================")

biscuit_list.insert("Milk", "Hide&Seek")

biscuit_list.display()

"""
data 5050
data_before None
new_node <node.Node object at 0x000001CE27916910>
5050
Goodday
Bourbon
Hide&Seek
Nutrichoice
=========================
data Milk
data_before Hide&Seek
new_node <node.Node object at 0x000001CE27916A10>
5050
Goodday
Bourbon
Hide&Seek
Milk
Nutrichoice
"""
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
                print(True)
                return temp
            temp=temp.get_next()
        return None
    
                                              
biscuit_list=LinkedList()
biscuit_list.add("Goodday")
biscuit_list.add("Bourbon")
biscuit_list.add("Hide&Seek")
biscuit_list.add("Nutrichoice")

biscuit_list.display()

biscuit_list.find_node("Bourbon")
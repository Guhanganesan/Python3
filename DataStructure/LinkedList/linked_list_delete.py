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
        print("data", data)
        print("data_before", data_before)
        print("new_node", new_node)
        
        if(data_before==None): # Add at 1st location
            new_node.set_next(self.__head) # self.__next = ??
            self.__head=new_node
            if(new_node.get_next()==None): # self.__next = ??
                self.__tail=new_node
    
        else: # Add after existing node 
            node_before=self.find_node(data_before)
            print("node_before: ", node_before)
            
            if(node_before is not None):
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if(new_node.get_next() is None):
                    self.__tail=new_node
            else:
                print(data_before,"is not present in the Linked list")
    
    def delete(self,data):
        node=self.find_node(data)
        if(node is not None):
            if(node==self.__head):
                if(self.__head==self.__tail):
                    self.__tail=None
                self.__head=node.get_next()
            else:
                temp=self.__head
                while(temp is not None):
                    if(temp.get_next()==node):
                        temp.set_next(node.get_next())
                        if(node==self.__tail):
                            self.__tail=temp
                        node.set_next(None)
                        break
                    temp=temp.get_next()
        else:
            print(data,"is not present in Linked list")
                                              
biscuit_list=LinkedList()
biscuit_list.add("Goodday")
biscuit_list.add("Bourbon")
biscuit_list.add("Hide&Seek")
biscuit_list.add("Nutrichoice")

print("=========================")

biscuit_list.delete("Bourbon")

biscuit_list.display()


#DSA-Exer-3
class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data

    def set_data(self,data):
        self.__data=data

    def get_next(self):
        return self.__next

    def set_next(self,next_node):
        self.__next=next_node


class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail


    def add(self,data):
        new_node=Node(data)
        if(self.__head is None):
            self.__head=self.__tail=new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail=new_node

    def insert(self,data,data_before):
        new_node=Node(data)
        if(data_before==None):
            new_node.set_next(self.__head)
            self.__head=new_node
            if(new_node.get_next()==None):
                self.__tail=new_node

        else:
            node_before=self.find_node(data_before)
            if(node_before is not None):
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if(new_node.get_next() is None):
                    self.__tail=new_node
            else:
                print(data_before,"is not present in the Linked list")

    def display(self):
        temp=self.__head
        sum=0
        count=1
        while(temp is not None):
            if(count%2!=0):
                sum=sum+temp.get_data()
            temp=temp.get_next()
            count+=1
        print(sum)
   
number_list=LinkedList()
number_list.add(10)
number_list.add(20)
number_list.add(30)
number_list.add(40)
number_list.add(50)
number_list.add(60)
number_list.add(70)
number_list.add(80)
number_list.add(90)
number_list.add(100)
number_list.add(110)

number_list.display()




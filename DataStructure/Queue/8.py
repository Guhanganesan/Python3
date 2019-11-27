"""
The TwinkleStar kindergarten kids are given a new game everyday to play among themselves. The teacher has come up with an idea for the kids to learn grouping and sorting. The teacher has given a container full of colored balls. Assume that the container has the following balls:

Color	Red	Blue	Yellow	Blue	Yellow	Green	Green	Red
Name	A	B	B	A	A	B	A	B
There are two each (A,B) of red, green ,blue and yellow balls in the container.
The task for the children is to take out the balls one at a time from the container and put it in four different containers based on the color. After that, the balls should be arranged such that the corresponding colored ball A is on top in all the four containers.

Note : The diameter of all the five containers are equal to that of a single ball, hence balls should be arranged one on top of the other.

Use the Ball class and list of balls to implement the class Game as given in the class diagram.

In the constructor of Game class create lists to store balls of different color separately
Display the color and name of the balls before and after grouping and arranging them in order.
Note: You may use the appropriate data structure(s) for solving this problem 
"""

#DSA-Assgn-12
class Queue:
    def __init__(self,max_size):

        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if(self.__rear==self.__max_size-1):
                return True
        return False

    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False

    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])


    def get_max_size(self):
        return self.__max_size

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data(Front to Rear): "+msg
        return msg

class Ball:
    def __init__(self,color,name):
        self.__color=color
        self.__name=name
        
    def __str__(self):
        return (self.__color+" "+self.__name)
    
    def get_color(self):
        return self.__color
    
    def get_name(self):
        return self.__name
             
#Implement Game class here
    
#Use different values to test your program
ball1=Ball("Red","A")
ball2=Ball("Blue","B")
ball3=Ball("Yellow","B")
ball4=Ball("Blue","A")
ball5=Ball("Yellow","A")
ball6=Ball("Green","B")
ball7=Ball("Green","A")
ball8=Ball("Red","B")
ball_list=Stack(8)
ball_list.push(ball1)  
ball_list.push(ball2) 
ball_list.push(ball3) 
ball_list.push(ball4) 
ball_list.push(ball5) 
ball_list.push(ball6) 
ball_list.push(ball7) 
ball_list.push(ball8)   

#Create objects of Game class, invoke the methods and test the program
                                                    

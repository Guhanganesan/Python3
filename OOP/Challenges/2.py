class Count:
    def __init__(self, count = 0):
       self.__count = count
 
c1 = Count(2)
c2 = Count(2)
print(id(c1) == id(c2)) # False
 
s1 = "Good"
s2 = "Good"
print(id(s1) == id(s2)) # True
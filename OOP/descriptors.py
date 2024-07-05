"""
Python descriptors are created to manage the attributes of different 
classes which use the object as reference.
"""
class Descriptor(object): 
  
    def __init__(self, name =''): 
        self.name = name 
  
    def __get__(self, obj, objtype): 
        return "{}for{}".format(self.name, self.name) 
  
    def __set__(self, obj, name): 
        if isinstance(name, str): # There is no type checking... so need to check
            self.name = name 
        else: 
            raise TypeError("Name should be string") 
          
class GFG(object): 
    name = Descriptor() 
    
g = GFG() 
g.name = "Computer"
print(g.name)

# https://www.datacamp.com/tutorial/python-descriptors

class Celsius(object):
    def __init__(self, value=0.0):
        self.value = float(value)
    def __get__(self, instance, owner):
        print("test")
        return self.value
    def __set__(self, instance, value):
        self.value = float(value)

class Temperature(object):
    celsius = Celsius()

temp=Temperature()
#calls celsius.__get__
temp.celsius = 45.5
print(temp.celsius) 

# 45.5

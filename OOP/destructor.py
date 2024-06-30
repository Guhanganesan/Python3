# Python program to illustrate destructor
class Employee:
 
    # Initializing
    def __init__(self):
        print('Employee created.')
        
    def hello(self):
        print("hello")
 
    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')
 
obj = Employee()
obj.hello()
# del obj

"""
Employee created.
hello
Destructor called, Employee deleted.
"""

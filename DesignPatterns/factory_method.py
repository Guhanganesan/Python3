"""
The Factory Method is used in object-oriented programming as a means to provide factory interfaces for creating objects. 
These interfaces define the generic structure, but don't initialize objects. The initialization is left to more specific subclasses.

The parent class/interface houses all the standard and generic behavior that can be shared across subclasses of different types. 
The subclass is in turn responsible for the definition and instantiation of the object based on the superclass.
"""

import abc
class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calculate_area(self):
        pass

    @abc.abstractmethod
    def calculate_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width 

    def calculate_perimeter(self):
        return 2 * (self.height + self.width) 

class Square(Shape):
    def __init__(self, width):
        self.width = width

    def calculate_area(self):
        return self.width ** 2

    def calculate_perimeter(self):
        return 4 * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius
    
class ShapeFactory:
    def create_shape(self, name):
        if name == 'circle':
            radius = input("Enter the radius of the circle: ")
            return Circle(float(radius))

        elif name == 'rectangle':
            height = input("Enter the height of the rectangle: ")
            width = input("Enter the width of the rectangle: ")
            return Rectangle(int(height), int(width))

        elif name == 'square':
            width = input("Enter the width of the square: ")
            return Square(int(width))
        
def shapes_client():
    shape_factory = ShapeFactory()
    shape_name = input("Enter the name of the shape: ")

    shape = shape_factory.create_shape(shape_name)

    print(f"The type of object created: {type(shape)}")
    print(f"The area of the {shape_name} is: {shape.calculate_area()}")
    print(f"The perimeter of the {shape_name} is: {shape.calculate_perimeter()}")

if __name__ == "__main__":
    shapes_client()

"""
Pros and Cons
Pros:-
One of the major advantages of using the Factory Method design pattern is that our code becomes loosely coupled in that the 
majority of the components of our code are unaware of other components of the same codebase.

This results in code that is easy to understand and test and adds more functionality to specific components 
without affecting or breaking the entire program.

The Factory Method design pattern also helps uphold the Single Responsibility Principle where classes and objects that 
handle specific functionality result in better code.

Cons:-
Creation of more classes eventually leads to less readability. If combined with an Abstract Factory (factory of factories), 
the code will soon become verbose, though, maintainable.

Conclusion:-
In conclusion, the Factory Method Design Pattern allows us to create objects without specifying the exact class required to 
create the particular object. This allows us to decouple our code and enhances its reusability.

It is important to note that, just like any other design pattern, it is only suitable for specific situations and not every 
development scenario. An assessment of the situation at hand is crucial before deciding to implement the Factory Method 
Design Pattern to reap the benefits of the pattern.
"""
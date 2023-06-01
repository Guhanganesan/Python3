"""
Classes (OOP) In object-oriented programming, a class is a blueprint for creating objects 
(a particular data structure), 
providing initial values for state 
(member variables or attributes), 
and implementations of behavior 
(member functions or methods)
Object-> properties: (color,weight,height)
      -> functions/methods : openGate(), closeGate()

"""

class Dept:     
    name="ECE" # class level variable
    year=4
    noStds=30


print(Dept.name)
print(Dept.year)
print(Dept.noStds)


class Calc:
    name="Casio"
    rate=200

    def add():
        print(10+20)
    
print(Calc.name)
print(Calc.rate)
Calc.add()

"""
The variable Dept.name is a class variable whose value is shared among all instances
of a this class. This can be accessed as Dept.name from inside the class or
outside the class.

The first method __init__() is a special method, which is called class constructor or
initialization method that Python calls when you create a new instance of this class.

Areas:

1. Inheritance
2. Encapsulation
3. Abstraction
4. Polymorphishm

Anvantages:

--> code reusability
-> memory consumption
-> execution time is less
-> security
"""
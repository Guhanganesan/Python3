"""
Classes (OOP) In object-oriented programming, 
a class is a blueprint for creating objects 
(a particular data structure), 
providing initial values for state (member variables or attributes), 
and implementations of behavior (member functions or methods)
Object-> properties: (color,weight,height)
      -> functions/methods : openGate(), closeGate()

"""

class Dept:     
    name="ECE"
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
Inheritance
Encapsulation
Abstraction
Polymorphishm

code reusability
->memory consumption
->execution time is less
->security
"""
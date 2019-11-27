class Car:
    def __init__(self, name):
        self.name = name
    
    def drive(self):
        pass
    def stop(self):
        pass
    
class Sportscar(Car):
    def drive(self):
        return 'Sportscar driving!'

    def stop(self):
        return 'Sportscar braking!'
    
class Truck(Car):
    def drive(self):
        return 'Truck driving slowly because heavily loaded.'

    def stop(self):
        return 'Truck braking!'

obj1=Truck('Bananatruck')
print(obj1.name)
print(obj1.drive())

obj1=Sportscar('Z3')
print(obj1.name)
print(obj1.drive())


class Rbi:
    def test(self):
        print("A")


class MyBank:
    def test(self):
        print("B")

class MyBranch(MyBank,Rbi):
    def go(self):
        print("Hi")
    

obj=MyBranch()
obj.test()
obj.go()


"""

class Vehicle:
    name="vehicle"
    def __init__(self):
        #print(self.name)
        pass
    def start(self):
        print("start")
#obj = Vehicle()
#obj.start()

class Truck():
    def turn_left(self):
        print("trun left")
        print(self.name)
#obj = Truck()
#obj.start()
#obj.turn_left()


class Cycle(Vehicle,Truck):
    def drive(self):
        print("drive")

obj=Cycle()
obj.start()
obj.turn_left()

"""

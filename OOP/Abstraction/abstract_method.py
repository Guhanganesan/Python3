from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        print("Hi")
    def stop(self):
        pass
    
# vc = Vehicle() #Can't instantiate abstract class Vehicle with abstract methods start
class Bus(Vehicle):
    def run(self):
        print('running')   
    def start(self):
        print("Starting")
    
obj = Bus()
obj.run()
obj.start()



    
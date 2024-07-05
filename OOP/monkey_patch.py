"""
Monkey patching is a technique that allows you to modify or extend the behavior of existing modules, classes, 
or functions at runtime without changing the original source code.
"""
class SomeClass(object):
    def __init__(self):
        self.a = 42
    def show(self):
        print(self.a)

def dosomething():
    sc = SomeClass()
    sc.show()
    
def new_init(self):
    self.a = 43

SomeClass.__init__ = new_init
dosomething()
#43


def add_speech(cls):
    cls.speak = lambda self, message: print(message)
    return cls


class Robot:
    def __init__(self, name):
        self.name = name

Robot = add_speech(Robot)

robot = Robot('Optimus Prime')
robot.speak('Hi')
print(robot.name)

# Hi
# Optimus Prime
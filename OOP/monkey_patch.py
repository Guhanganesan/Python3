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

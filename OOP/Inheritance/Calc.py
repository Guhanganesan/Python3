class MasterCalc:
    name="Casio"
    def __init__(self):
        self.x=0
        self.y=0
    def test(self,a,b):
        self.x=a
        self.y=b
        print(self.x+self.y)
    def add(self,a,b):
        pass
    def sub(self,a,b):
        pass
    def sin(self):
        pass

class BasicCalc(MasterCalc):
    pass

obj=BasicCalc()
obj.test(20,10)






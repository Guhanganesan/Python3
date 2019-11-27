class Rbi:#Data Hiding
    _area="Chennai" #protected 
    __mob=768767    #private
    def __init__(self):
        self.__pin=12345
        self.name="RBI"
        print(self.__mob, self._area)
    def getValues(self):
        print(self.name, self.__pin)
    
    def __rate(self): 
        print("Rate is 10%")
    def add(self):
        self.__rate()

obj=Rbi()
obj.getValues()
print(obj._area)
#print(obj.__mob) #AttributeError: 'Rbi' object has no attribute '__mob'
#obj.add()
#obj.__rate() #AttributeError: 'Rbi' object has no attribute '__rate'

class MyBank(Rbi):
     def __init__(self):
        print(self._area)
        #print(self.__mob) #cannot print
        self.add()
        #self.__rate()


obj=MyBank()
print(obj._area)
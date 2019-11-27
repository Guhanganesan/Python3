class Mobile:
    def setValues(self,price,brand):
        self.price = price
        self.brand = brand

    def getValues(self):
        print (self.price)
        print (self.brand)

obj =Mobile()
obj.setValues(10000,"Mobile")
obj.getValues()

class Nokia(Mobile):
    def __init__(self):
        super().setValues(12000,"Nokia")

    def getValues(self):
        print(self.price)
        print(self.brand)

nk =Nokia()
nk.getValues()



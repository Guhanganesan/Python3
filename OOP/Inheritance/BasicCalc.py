import Calc
class BasicCalc(Calc):
      def test(self):
          print(self.x)
obj1=Calc()
obj1.test(10,20)

obj2=BasicCalc()
obj2.test()

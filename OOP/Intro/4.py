class Calc:
    def add(a,b):
        x=a
        y=b
        return x+y
    def test():
        print(x) #the name x is not defined
        print(y) #the name y is not defined


res = Calc.add(20,10) 
print(res)
Calc.test()




class Agni:
    def collect_fees(self):
        print("fees is 10000")
    def collect_fees(self,a, b):#overload
        self.a=a
        self.b=b
        print("fees is 10000", self.a, self.b)
    
obj = Agni()
#obj.collect_fees()
obj.collect_fees(100,0)

class Branch(Agni):

    def collect_fees(self,a, b, c):#override
        self.a=a
        self.b=b
        self.c=c
        print("fees is 10000", self.a, self.b, self.c)

branch = Branch()
branch.collect_fees(20,30, 70)


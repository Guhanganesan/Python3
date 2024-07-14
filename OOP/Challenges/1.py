class father:
    def __init__(self, param):
        self.o1 = param
 
class child(father):
    def __init__(self, param):
        super().__init__(20)
        self.o2 = param
 
obj = child(22)
print ("%d %d" % (obj.o1, obj.o2))
# AttributeError: 'child' object has no attribute 'o1' if super() is not invoked
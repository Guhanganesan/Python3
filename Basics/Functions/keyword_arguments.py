def reg(name, age=20):
    print(name," and ", age)

reg(name="Guhan",age=30)
reg("Raja", 24)
reg(age=23, name="Anbu")
reg(name="Anbu")

#-----------------------------

def register(*args):
    for index in args:
        print(index)

register(10, 20, "Guhan", "guhan@gmail.com")

#----------------------------

def regDetails(**kwars):
    #print(kwars)
    for key, value in kwars.items():
        print(key, value)

regDetails(name="Guhan", age =25, mobile=97971, area="Chennai")



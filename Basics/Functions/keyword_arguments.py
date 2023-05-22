"""
def example(a, b, c=None, r="w", d=[], *ae,  **ab):

(a,b) are positional parameter

(c=none) is optional parameter

(r="w") is keyword parameter

(d=[]) is list parameter

(*ae) is keyword-only

(*ab) is var-keyword parameter

"""
def reg(name, age=20):
    print(name," and ", age)

reg(name="Guhan",age=30)
reg("Raja", 24)
reg(age=23, name="Anbu")
reg(name="Anbu")

#---------------- Arbitrary Arguments-------------

def register(*args):
    for index in args:
        print(index)

register(10, 20, "Guhan", "guhan@gmail.com")

#------------------Keyword arguments ----------

def reg_details(**kwars):
    #print(kwars)
    for key, value in kwars.items():
        print(key, value)

reg_details(name="Guhan", age =25, mobile=97971, area="Chennai")



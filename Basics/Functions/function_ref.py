x=10
def add():
    global x
    x=20
    print(x)
add()
print(x)

#================

def test(a,b,c=None,d=None):
    if a and b and not(c) and not(d):
        print(a+b)
    elif a and b and c and not(d):
        print(a+b+c)
    elif a and b and c and d:
        print(a+b+c+d)
        
#  test() # test() missing 2 required positional arguments: 'a' and 'b'

test(10,20)
test(10,20,30)
test(10,20,30,40)

Ans:
30
60
100

#==================

def divide(num):
    return num/2 
    

for num in [30,20,40,50,60]:
    res= divide(num)
    print(res)


#==================


def divide(num):
    return num/2 
    

res = map(divide, [30,20,40,50,60])
print(list(res))

#==================


def check_name(name):
    
    return "Guhan" in name 
    
res = list(map(check_name, ['Guhan', 'Anbu', 'Murugan', 'Guhan Ganesan']))
print(res)


Ans: [True, False, False, True]

#=========================

def check_name(name):
    
    return "Guhan" in name 
    
res = list(filter(check_name, ['Guhan', 'Anbu', 'Murugan', 'Guhan Ganesan']))
print(res)

Ans: ['Guhan', 'Guhan Ganesan']

#=========================

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = dict(zip(a, b))
print(x)

#=========================

def countdown(n):
    print(n)
    if n==0:
        return
    else:
        countdown(n-1)
countdown(5)

#==========================

def factorial(n):
    if n<=1:
        return 1 
    else:
        return n * factorial(n-1)
        
res = factorial(5)
print(res)

#==========================









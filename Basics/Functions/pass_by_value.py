L=[1,2,3,4,5]
y=100

def test(x):
    x[1] = 100
    #y = 200 #Un used local variable -> There is no change in global variable
    global y
    y = y+300

test(L)
print(L)
print(y)

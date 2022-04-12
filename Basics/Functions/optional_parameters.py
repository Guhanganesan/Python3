a = 10
b = 20

def test_optional_parameters(a, b, c=None, d=None):
    print(a)
    print(b)
    print(c)
    print(d)


#test_optional_parameters(a) # test_optional_parameters() missing 1 required positional argument: 'b'
test_optional_parameters(a,b) # required a and b
test_optional_parameters(10, 40, 'Hello')
test_optional_parameters(10, 40, 'Hello', 'Welcome')

"""
Answer:
10
20
None
None
10
40
Hello
None
10
40
Hello
Welcome
"""
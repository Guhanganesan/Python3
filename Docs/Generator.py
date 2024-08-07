def test():
    yield 1
    yield 2 
    
for data in test():
    print(data)
    
elem = iter(test())
# while True:
#     if next(elem):
#         print(next(elem))
#     else:
#         break
    
while element:= next(elem, False):
    print(element)
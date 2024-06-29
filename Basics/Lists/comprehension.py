a="guhan"
b="12345"
z=[ "".join([list(b)[i],list(a)[i]]) for i in range(0,len(list(a)))]
print("".join(z))

# 1g2u3h4a5n

a='guhan'
z=list(map(lambda char: char+'10', [char for char in a]))
print(z) # ['g10', 'u10', 'h10', 'a10', 'n10']

lis = [i**2 if i % 2 == 0 
       else i**3 for i in range(8)] 
print(lis) # [0, 1, 4, 27, 16, 125, 36, 343]

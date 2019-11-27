a={1,4,2,5,7,9}
b={3,6,2,8,7,10}
c={1,2,5}
d={22,11}

print(a.union(b))
print(a.intersection(b))
print(c.issubset(a))
print(d.isdisjoint(a))
print(a.issuperset(c))
print(a.difference(b)) 
print(a.symmetric_difference(b)) 

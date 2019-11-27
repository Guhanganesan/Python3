d={'name':'guhan','mob':87578}
print(d)
d.update({'age':27})
print(d)
d.pop("age")
print(d)
d.popitem()
print(d)
d.update({'age':27})
d.update({'mob':5465})
print(d)
print(d['age'])
d['age']=30
print(d)
d.update({'age':45})
print(d)
for i in d:
    print(i)
for i in d.keys():
    print(i)

for i in d.values():
    print(i)

for i,j in d.items():
    print(i,j)

d=dict([('name','anbu'),('age',28)])
print(d)
d={'name':'anbu','age':27}
print(d)

d.update({'mob':9869869}) #update same key not includes new key
print(d)

print(d['name'])
d['name']='raja'
print(d)

print(d.get('name'))

d.pop('age')
print(d)

d.popitem() #removes from last key and values
print(d)

d={'a':1, 'b':2}
del d['b']
print(d)


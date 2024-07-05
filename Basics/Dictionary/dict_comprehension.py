names=['guhan','anbu','amudhan','jayasri']
ages=[34,32,2,31]
d = dict(zip(names,ages))
print(d) # {'guhan': 34, 'anbu': 32, 'amudhan': 2, 'jayasri': 31}

d= {k:v for k,v in zip(names,ages)}
print(d) # {'guhan': 34, 'anbu': 32, 'amudhan': 2, 'jayasri': 31}

keys=dict.fromkeys(range(5), True)
print(keys)

#Frame Keys
d_names = [{"name":val} for val in names]
print(d_names) # [{'name': 'guhan'}, {'name': 'anbu'}, {'name': 'amudhan'}, {'name': 'jayasri'}]

# Frame Dicts
d_ = [{"name":key,"age":val} for key, val in zip(names,ages)]
print(d_) # [{'name': 'guhan', 'age': 34}, {'name': 'anbu', 'age': 32}, {'name': 'amudhan', 'age': 2}, {'name': 'jayasri', 'age': 31}]

newdict = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(newdict) # {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}

W="Program finished with exit code 0"
# 0, code, exit, with, Program
# 1: 0, 
# 4 : 3

words = W.split(" ")
w_count = {s:words.count(s) for s in words}
print(w_count) 
# {'Program': 1, 'finished': 1, 'with': 1, 'exit': 1, 'code': 1, '0': 1}

w_count = {s:len(s) for s in words}
print(w_count)

# {'Program': 7, 'finished': 8, 'with': 4, 'exit': 4, 'code': 4, '0': 1}

areas=['R','K','F']
# Frame Dicts
d_ = [{"name":key,"age":val, "areas":mz} for key, val, mz in zip(names,ages, areas)]
print(d_) # [{'name': 'guhan', 'age': 34, 'areas': 'R'}, {'name': 'anbu', 'age': 32, 'areas': 'K'}, {'name': 'amudhan', 'age': 2, 'areas': 'F'}]

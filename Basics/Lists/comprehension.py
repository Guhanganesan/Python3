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

string = 'GuhanGanesan'
# Toggle case of each character 
# a = 97
# A = 65 
# Diff = 97-65 = 32
# ^ => (-65) = 65
List = list(map(lambda i: chr(ord(i)^32), string))
print("".join(List)) # gUHANgANESAN

names = ["G", "G", "g"] 
ages = [25, 30, 35] 
person_tuples = [ (name, str(age)) for name, age in zip(names, ages)] 
print(person_tuples) # [('G', '25'), ('G', '30'), ('g', '35')]

x=('a','b')
y="".join(x)
print(y) # ab 

z = "".join(["".join(i) for i in person_tuples])
print(z) # G25G30g35

person_dict = [{key:val} for key, val in zip(names,ages)]
print(person_dict) #[{'G': 25}, {'G': 30}, {'g': 35}]

z=dict(zip(names,ages))
print(z) # {'G': 30, 'g': 35} duplicate key removed







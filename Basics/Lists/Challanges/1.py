L1=[10]
L2=L1
L2[0]=80
print(L1) # 80
print(L2) # 80

names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
names2 = names1
names3 = names1[:]
names2[0] = 'Alice'
names3[1] = 'Bob'
 
sum = 0
for ls in (names1, names2, names3):
    print(ls)
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
        sum += 10
print(sum) # 12

"""
['Alice', 'Bear', 'Charlton', 'Daman']
['Alice', 'Bear', 'Charlton', 'Daman']
['Amir', 'Bob', 'Charlton', 'Daman']
12
"""
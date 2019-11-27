#List Methods
L=[]
list=["A","B","C","D","E"]
print(list[0])
print(list[0:3])
print(list[-3:-1])
print(list[::-1])#reverse
print(list[2:])
print(list[:4])

print(len(list))

list.pop()
print(list)

list.append("F")
print(list)

list.pop(1)
print(list)

list.insert(1,"K")
print(list)

del(list[0])
print(list)

list.extend(["L","M","N"])
print(list)

del(list[2])
print(list)

list.remove("K")
print(list)

list.reverse()
print(list)

print(list.count("M"))
copy=list.copy()
print(copy)
clear=copy.clear()
print(clear)

list.sort()
print(list)

print(list.__contains__("D"))
list.__delitem__(0)

print(list) 
item=list.__getitem__(0)

print(item)
L=[1,2,3]
del(L[0])
print(L)

L[1]="Z"
print(L)

L=["T","E","M","S","B"]
L.append("C")
print(L)

L.insert(2,"Z")
print(L)

L.extend(["F","G"])
print(L)

L.insert(5,"D")
print(L)

L.pop()
print(L)

L.pop(4)
print(L)

L.remove("Z")
print(L)

L.reverse()
print(L)

L.sort()
print(L)

print(L.index("E"))

print(L.count("C"))

print(len(L))

del(L[3])
print(L)





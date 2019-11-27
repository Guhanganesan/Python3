user =int(input("Enter Value"))
#print(user)#45
L=[34,45,67,76,54,32]
check=False
for i in range(0,len(L)):
    if user==L[i]:
        print("Found at: ", (i+1))
        check=True
        break
if(check==False):
    print("Not Found")
"""
L=[45,34,23,56,78]
length=len(L)
print(length)
user=int(input("Enter Value"))
for i in range(0, length):
    if user==L[i]:
        L.remove(user)
        break
        #length=length-1
print(L)
"""

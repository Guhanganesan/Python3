L=[23,45,56,78,43]
check=False
element=int(input("Enter Element to Remove"))
for i in range(0,len(L)):#0,5
    if element==L[i]:
        L.remove(element)
        check=True
        break
if(check==False):
    print("Not Found")      

print(L)


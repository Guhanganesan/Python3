
try:
    L=[10,20,30,40]
    print(L[5])
    #length=len(L) #4
    #for i in L:
    #   print(i)

    for i in range(0,6):
        print(L[i])

except IndexError as e:
    print("The range of list is exceeds",e)


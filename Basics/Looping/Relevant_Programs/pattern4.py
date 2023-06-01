for i in range(5,0,-1): 
    for s in range(5,i,-1):
        print(" ", end=" ")
    for j in range(1,(i+1)):
        print(j, end=" ")
    print()

for i in range(2,6): 
    for s in range(5,i,-1):
        print(" ", end=" ")
    for j in range(1,(i+1)):
        print(j, end=" ")
    print()


"""

1 2 3 4 5 
  1 2 3 4 
    1 2 3 
      1 2 
        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5 

"""
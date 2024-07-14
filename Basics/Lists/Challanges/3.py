myList = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    print("i - 1 = ", (i-1))
    myList[i - 1] = myList[i] 
    # updated upto index 4 [2 3 4 5 6] last index not updated
 
for i in range(0, 6): 
    print(myList[i], end = " ") # 2 3 4 5 6 6 
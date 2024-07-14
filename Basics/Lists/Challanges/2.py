myList = [1, 5, 5, 5, 5, 1]
max = myList[0]
indexOfMax = 0
for i in range(1, len(myList)):
    if myList[i] > max: # 5>1, 5>5.. 1>1
        max = myList[i]
        indexOfMax = i # 1
print(indexOfMax) # 1
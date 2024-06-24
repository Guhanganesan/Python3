import copy
li1 = [1, 2, [3,5], 4]
li2 = copy.deepcopy(li1)
li2[2][0] = 7
print(li2) # [1, 2, [7, 5], 4]
print(li1) # [1, 2, [3, 5], 4]


li1 = [1, 2, [3,5], 4]
li2 = copy.copy(li1)
li2[2][0] = 7
print(li1) # [1, 2, [7, 5], 4]

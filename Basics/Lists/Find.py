# Find elements of a list by indices present in another list

def findElements(lst1, idex_lst2):
	return list(map(lst1.__getitem__, idex_lst2))
			
# Driver code
lst1 = [10, 20, 30, 40, 50]
idex_lst2 = [0, 2, 4]
print(findElements(lst1, idex_lst2))

# [10, 30, 50]

# Example 2

# Python3 program to Find elements of a 
# list by indices present in another list
from operator import itemgetter 

def findElements(lst1, lst2):
	return list((itemgetter(*lst2)(lst1)))
			
# Driver code
lst1 = [10, 20, 30, 40, 50]
lst2 = [0, 2, 4]
print(findElements(lst1, lst2))


# Example 3

# Find elements of a list by indices present in another list
import numpy as np 

def findElements(lst1, lst2):
	return list(np.array(lst1)[lst2])
			
# Driver code
lst1 = [10, 20, 30, 40, 50]
lst2 = [0, 2, 4]
print(findElements(lst1, lst2))


# Example 4 

def findElements(lst1, lst2):
	# Create a dictionary that maps indices in lst2 to their corresponding elements in lst1
	index_map = {index: element for index, element in enumerate(lst1)}
	
	# Use a list comprehension to extract the values from the dictionary
	return [index_map[index] for index in lst2]

lst1 = [10, 20, 30, 40, 50]
lst2 = [0, 2, 4]
print(findElements(lst1, lst2))

#This code is contributed by Edula Vinay Kumar Reddy

# Example Recursive Method ***********

def findElements(lst1, lst2, idx=0, res=[]):
	if idx == len(lst2):
		return res
	res.append(lst1[lst2[idx]])
	return findElements(lst1, lst2, idx+1, res)
lst1 = [10, 20, 30, 40, 50]
lst2 = [0, 2, 4]
res = findElements(lst1, lst2)
print(res)


# Example 5

# assign list
import operator
l = [1, 2.0, 'have', 'a', 'geeky', 'day']
# assign string
s = 'geeky'
# check if string is present in the list
if operator.contains(l, s):
	print(f'{s} is present in the list')
else:
	print(f'{s} is not present in the list')


# Example 6 

import re

# assign list
l = [1, 2.0, 'have', 'a', 'geeky', 'day']

# assign string
s = 'geeky'

# check if string is present in each string in the list
for item in l:
	if isinstance(item, str) and re.search(s, item):
		print(f'{s} is present in the list')
		break
else:
	print(f'{s} is not present in the list')
# This code is contributed by Vinay Pinjala.


# Example 7 

# initializing list
test_list = [1, 3, 4, 3, 6, 7]

# printing initial list
print("Original list : " + str(test_list))

# using filter() to find indices for 3
res_list = list(filter(lambda x: test_list[x] == 3, range(len(test_list))))

# printing resultant list
print("New indices list : " + str(res_list)) # New indices list : [1, 3]








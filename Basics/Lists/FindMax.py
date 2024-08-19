# Example 1

square = {2: 4, -3: 9, -1: 1, -2: 4}

# the largest key
key1 = max(square)
print("The largest key:", key1)    # 2
# the key whose value is the largest
key2 = max(square, key = lambda k: square[k])
print("The key with the largest value:", key2)    # -3
# getting the largest value
print("The largest value:", square[key2])    # 9


# Example 2 

# Program to find most frequent 
# element in a list
def most_frequent(List):
	return max(set(List), key = List.count) # passing elements {2,1,3} => 3,2,1 => key = passed element

List = [2, 1, 2, 2, 1, 3]
print(most_frequent(List))



# Example 3 

# Program to find most frequent 
# element in a list

from collections import Counter

def most_frequent(List):
	occurence_count = Counter(List)
	return occurence_count.most_common(1)[0][0]

List = [2, 1, 2, 2, 1, 3]
print(most_frequent(List))


# Example 4 

import statistics
from statistics import mode

def most_common(List):
	return(mode(List))

List = [2, 1, 2, 2, 1, 3]
print(most_common(List))





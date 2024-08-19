# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(newList):
    size = len(newList)
    
    # Swapping 
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
    
    return newList
    
# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))

####################################################################

# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(newList):
    
    newList[0], newList[-1] = newList[-1], newList[0]

    return newList
    
# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))

####################################################################


# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(list):
    
    # Storing the first and last element 
    # as a pair in a tuple variable get
    get = list[-1], list[0]
    
    # unpacking those elements
    list[0], list[-1] = get
    
    return list
    
# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))

####################################################################

# Python3 program to illustrate 
# the usage of * operand
list = [1, 2, 3, 4]

a, *b, c = list

print(a)
print(b)
print(c)


####################################################################


# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(list):
    
    start, *middle, end = list
    list = [end, *middle, start]
    
    return list
    
# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))


####################################################################

# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(list):
    
    first = list.pop(0)   
    last = list.pop(-1)
    
    list.insert(0, last)  
    list.append(first)   
    
    return list
    
# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))


####################################################################

def swap_first_last_3(lst):
    # Check if list has at least 2 elements
    if len(lst) >= 2:
        # Swap the first and last elements using slicing
        lst = lst[-1:] + lst[1:-1] + lst[:1]
    return lst

# Initializing the input
inp=[12, 35, 9, 56, 24]

# Printing the original input
print("The original input is:",inp)

result=swap_first_last_3(inp)

# Printing the result
print("The output after swap first and last is:",result)

####################################################################

# Sample string
my_string = "hello"# Convert string to list
my_list = list(my_string)# Swap first and last characters
my_list[0], my_list[-1] = my_list[-1], my_list[0]# Convert list back to string
new_string = "".join(my_list)


# Sample list
my_list = [1, 2, 3, 4, 5]
# Move the first element to the end
my_list.append(my_list.pop(0))


# Sample list
my_list = [1, 2, 3, 4, 5]
# Shift elements to the left by one position
shifted_list = my_list[1:] + [my_list[0]]


# Sample string
my_string = "hello"
# Switch first and last characters
new_string = my_string[-1] + my_string[1:-1] + my_string[0]



# Python3 program to swap elements
# at given positions

# Swap function
def swapPositions(lis, pos1, pos2):
	temp=lis[pos1]
	lis[pos1]=lis[pos2]
	lis[pos2]=temp
	return lis
# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1-1, pos2-1))







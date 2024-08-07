# Program to find most frequent 
# element in a list

def most_frequent(List):
	temp = 0
	num = List[0]
	
	for elem in List:
		curr_frequency = List.count(elem)
		if(curr_frequency> temp):
			temp = curr_frequency
			num = elem
	return num

List = [2, 1, 2, 2, 1, 3]
print(most_frequent(List)) # 2 
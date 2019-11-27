def Binary_search(arr,start_index,last_index,element):
	while (start_index<= last_index):
		mid =(int)(start_index+last_index)//2
		if (element>arr[mid]):
			start_index = mid+1
		elif (element<arr[mid]):
			last_index = mid-1
		elif (element == arr[mid]):
			return mid
	return -1
	
arr = [2,14,19,21,99,210,512,1028,4443,5110]
element = 4443
start_index = 0
last_index = len(arr)-1
found = Binary_search(arr,start_index,last_index,element)
if (found == -1):
	print("element not present in array")
else:
	print("element is present at index ", str(found))
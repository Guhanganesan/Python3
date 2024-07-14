# Sort dictionary Keys
data = {'D': 'red', 'B': 'green', 'A': 'yellow', 'C': 'orange'}
sorted_list = sorted(data)
print(sorted_list) # ['A', 'B', 'C', 'D'] # sorted keys

temp_dict={}
for item in sorted_list:
    temp_dict[item]=data[item]  # update dict = get dict

print(temp_dict) # {'A': 'yellow', 'B': 'green', 'C': 'orange', 'D': 'red'}
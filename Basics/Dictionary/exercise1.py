W="Program finished with exit code 0"
# 0, code, exit, with, Program
# 1: 0, 
# 4 : 3

words = W.split(" ")
print(words)
d_count = {}
l_count = [len(s) for s in words]
print(l_count)

temp=0 #8
temp_c=0
for num in l_count:
    if temp != num: # 7, 8 
        temp = num
        temp_c=0
    if temp == num:
        temp_c=temp_c+1
        d_count[num]=temp_c 
    
print(d_count)

# Alternate 

l_count = [{s:words.count(s)} for s in words]
print(l_count) 
# [{'Program': 1}, {'finished': 1}, {'with': 1}, {'exit': 1}, {'code': 1}, {'0': 1}]

for data in l_count:
    d_count.update(data)
print(d_count)
# {'Program': 1, 'finished': 1, 'with': 1, 'exit': 1, 'code': 1, '0': 1}

l_count = [{s:len(s)} for s in words]
print(l_count)
for data in l_count:
    d_count.update(data)
print(d_count)

# {'Program': 7, 'finished': 8, 'with': 4, 'exit': 4, 'code': 4, '0': 1}
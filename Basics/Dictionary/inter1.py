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

print(list(d_count.keys()))

keys=list(d_count.keys())

# d_words = [  for k in keys if k in len(words)]

""" 
Find cumulative sum of the list where the i'th element is the 
sum of the first i+1 elements from the original list.

Cumulative Sum: [1,2,3,4,5] = [1,3,6,10,15]
num=> num+sum 
1 => 1+0 => 1 [1]
2 => 2+1 => 3 [1,3]
3 => 3+3 => 6 [1,3,6]
4 => 4+6 => 10 [1,3,6,10]
5 => 5+10 => 15 [1,3,6,10,15]
"""

L=[1,2,3,4,5]
temp = 0
sum_list = []

for num in L:
    temp=temp+num 
    sum_list.append(temp)

print(sum_list)

res = [sum(L[0:index+1]) for index in range(0, len(L))]
print(res)




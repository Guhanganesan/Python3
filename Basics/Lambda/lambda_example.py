def fun(x,y):
    return x+y

res=fun(10,20)
print(res)

myvar = lambda x,y: x+y 
print(myvar(10,20))

calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"
 
print(calc(20)) #Even number

filter_nums = lambda s: ''.join([ch for ch in s if not ch.isdigit()])
print("filter_nums():", filter_nums("Guhan101")) # Guhan

find_sum = lambda n: sum([int(x) for x in str(n)])
print("find_sum():", find_sum(101)) #2

# Sort 
l = ["1", "2", "9", "0", "-1", "-2","4"]

print(lambda x: int(x)) # <function <lambda> at 0x789b83fc0680>

print(sorted(l, key=lambda x: int(x))) # ['-2', '-1', '0', '1', '2', '4', '9']
 
# Positive even numbers
print(list(filter(lambda x: not (int(x) % 2 != 0 and int(x) > 0), l))) # ['2', '0', '-1', '-2', '4']
 
# added 10 to each item after type and
# casting to int, then convert items to string again
print(list(map(lambda x: str(int(x) + 10), l)))
# ['11', '12', '19', '10', '9', '8', '14']


# Python program showing
# using of normal function
def Key(x):
    return x%2
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sort = sorted(nums, key = Key)
print(sort) # [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sort_lambda = sorted(nums, key = lambda x: x%2)
print(sort_lambda) # [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]

# Difference between Filter, Map, Lambda

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
def even(num):
    if num%2 == 0:
        return True
    return False

for num in nums:
    print(even(num),end=" ")
# False True False True False True False True False True    
print()

print(list(map(even,nums))) 
# [False, True, False, True, False, True, False, True, False, True]

print(list(filter(even,nums))) 
# [2, 4, 6, 8, 0]

# using filter() function
evens = filter(lambda x: True if (x % 2 == 0) else False, nums)
print(list(evens)) # [2, 4, 6, 8, 0]

#Overuse Lambda Expression

d = (lambda x, y, z: x*y+z)(1, 2, 3)
print(d) # 5

num = (lambda x: "one" if x == 1 else( "two" if x == 2
                       else ("three" if x == 3 else "ten")))(3)
print(num) #three

nums = [-2, -1, 0, 1, 2]
sort = sorted(nums, key=lambda x: abs(x))
print(sort) # [0, -1, 1, -2, 2]

sort = sorted(nums, key=abs) # Enough
print(sort) # [0, -1, 1, -2, 2]


print((x for x in range(5))) # <generator object <genexpr> at 0x7eff6990e4d0>
print([x for x in range(5)]) # [0, 1, 2, 3, 4]



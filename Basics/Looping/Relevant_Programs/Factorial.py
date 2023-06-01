"""
t=1
   1*1=1
   1*2=2
   2*3=6
   6*4=24
   24*5=120
   t*count=t
Eq:
t=t*count  => 
5x(5-1)x(5-2)x(5-3)x(5-4)
    = 5x(5-1)
    = 
"""

start=1
for i in range(start,6):
    start=start*i

print(start)


# Using Recursion
def find_fact(num):
    if num == 1:
        return num
    else:
        num = num * find_fact(num-1)
        print(num)
        return num

res = find_fact(5)
print("Factorial: ", res)



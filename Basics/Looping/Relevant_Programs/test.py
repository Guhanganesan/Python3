# 0 1 1 2 3 5 8 13...
f=0
s=1

"""
f  +  s = n
0  +  1 = 1
f=s
s=n
1  +  1 = 2

1  +  2 = 3

2  +  3 = 5

3   + 5 = 8

"""

for i in range(1, 9):
    print(f)
    n=f+s
    f=s
    s=n








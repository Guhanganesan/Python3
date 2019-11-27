# 0, 1, 1, 2, 3, 5, 8..

first=0
second=1
i=0
while i<8:
    print(first)
    next=first+second
    first=second
    second=next
    i=i+1

"""
next=f+s

0 + 1 = 1

1 + 1 = 2

1 + 2 = 3

2 + 3 = 5

3 + 5 = 8

"""


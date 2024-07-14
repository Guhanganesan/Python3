import itertools
data = {'1':['a', 'b'], '2':['c','d']}

l = [ data[k] for k in sorted(data.keys())]
print(l) # [['a', 'b'], ['c', 'd']]

for combo in itertools.product(*l):
    print(" ".join(combo))

"""
a c
a d
b c
b d
"""



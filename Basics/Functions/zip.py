column = ("name", "age", "mobile")
row = ("Raja", "26", 43884343)

res = zip(column, row)

data = dict(tuple(res))

print(data)

"""
{'name': 'Raja', 'age': '26', 'mobile': 43884343}
"""
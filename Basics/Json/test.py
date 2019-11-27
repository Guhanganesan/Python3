import json
with open('myjson.json') as f:
     m =json.load(f)
     print(m)

data='{"name":"raja","mobile":87878,"age":25}'
m=json.loads(data)
print(m)
for i in m:
    print(i)

for i in m.values():
    print(i)

for i,j in m.items():
    print(i,j)


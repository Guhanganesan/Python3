import json
with open('myfile.json') as f:
    #print(f)
    data = json.load(f)
#print(data)

for i in data.values():
    print(i) 


#for i,j in data.items():
    #print(i,j)

#d = {"name":"raja","mob":876876,"age":26}

#m=json.dumps(d)
#m=json.dumps(d,indent=True,separators=('.','='))
#print(m)


"""
{'name': 'anbu', 'mobile': 8976986, 'age': 25, 'email': 'anbu@gmail.com'}
anbu
8976986
25
anbu@gmail.com
name anbu
mobile 8976986
age 25
email anbu@gmail.com
{"name": "raja", "mob": 876876, "age": 26}
"""
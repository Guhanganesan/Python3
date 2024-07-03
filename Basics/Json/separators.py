import json
#L=[10,12,15]
d={'name':'anbu','age':27,'mob':76327}
#data=json.dumps(d)  
#data=json.dumps(d, indent=True) #json 
#data=json.dumps(d, indent=10) #for space
#data=json.dumps(d, indent=True,sort_keys=True)
data=json.dumps(d,indent=4,separators=(".", " = "))
print(data)

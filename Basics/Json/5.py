#delete data
import json
with open('myfile.json','r') as f:
    #print(f)
    data = json.load(f)
    
for element in data:
    #print(element)
    if 'id' in element:
       del data['id']
       break

with open('myfile.json', 'w') as data_file:
    data = json.dump(data, data_file)


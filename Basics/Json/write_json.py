#update data
import json
with open('myfile.json','r+') as f:
    #print(f)
    data = json.load(f)
    data['id']=1
    data['name']="Raja"
    f.seek(0)
    json.dump(data, f, indent=4)
    #f.truncate()
# mode r+ --> file write


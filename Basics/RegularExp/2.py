#check only 2 chars inbetween A nd l
import re
if(re.search(r"A..l","Aopline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

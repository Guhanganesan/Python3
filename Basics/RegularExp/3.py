#To search for a digit between A and l in 
# the given string "A2line".
import re
if(re.search(r"A\dl","A2line")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

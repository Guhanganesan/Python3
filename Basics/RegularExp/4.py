#To search for a number between 4 and 8 in between A and l in the given string.
import re
if(re.search(r"A[4-8]l","A5line")!=None):
    print("Pattern found")
else:
    print("Pattern not found")


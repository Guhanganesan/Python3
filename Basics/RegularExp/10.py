#To check if 3 digits are present after A in the given string
import re
if(re.search(r"A\d{3}i","A2224irline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")


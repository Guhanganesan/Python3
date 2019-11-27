#To check if a number is found 0 or 1 times after A in the given string
import re
if(re.search(r"A\d?i","A23irline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

#To check if a number is found 0 or n times after A in the given string.
import re
if(re.search(r"A\d*","A2234line")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

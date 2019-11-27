#To check whether last character is alphanumeric or not.
import re
if(re.search(r"\w$","Airline%")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

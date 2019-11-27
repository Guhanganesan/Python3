#To check for the space after "Air" in the given string "Airline".
import re
if(re.search(r"Air\s","Air line")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

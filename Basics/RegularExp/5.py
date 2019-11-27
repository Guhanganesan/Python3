#To search for the pattern "Hell" or "Fell" in the given string "Fellow".
import re
if(re.search(r"Hell|Fell","Fellow")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

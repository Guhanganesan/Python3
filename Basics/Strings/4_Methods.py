x="QWERTY" #immutable->can't be changed

print("Lnegth: ", len(x))

print("Lower: ",x.lower())

print("Upper: ",x.upper())

print("Capitalize: ",x.capitalize())

print("Swapcase: ",x.swapcase()) #if lower means upper, upper means lower

print("Center: ",x.center(8,' '))
# **QWERTY**
print("Count: ",x.count('Q'))

print("Find: ",x.find('W')) # found 1

print("Find: ",x.find('Z')) # not found -1

print("Index: ",x.index('E'))

s=("Sangavi","Bala")
print(" ".join(s))

data="   ABCD   --- ABCD  ---"
print("Strip: ",data.strip())
print("Left Strip: ",data.lstrip("-"))
print("Right Strip: ",data.rstrip("-"))
print("Both Strip: ",data.strip(" ")) #strip both left and right

print("Split: ",x.split()) #list of substring

print("Replace: ",x.replace("Q","P"))

"""
Lnegth:  6
Lower:  qwerty
Upper:  QWERTY
Capitalize:  Qwerty
Swapcase:  qwerty
Center:   QWERTY 
Count:  1
Find:  1
Find:  -1
Index:  2
Sangavi Bala
Strip:  ABCD   --- ABCD  ---
Left Strip:     ABCD   --- ABCD  ---
Right Strip:     ABCD   --- ABCD  
Both Strip:  ABCD   --- ABCD  ---
Split:  ['QWERTY']
Replace:  PWERTY

"""
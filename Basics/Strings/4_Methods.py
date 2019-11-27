x="QWERTY" #immutable->can't be changed

print(len(x))

print(x.lower())

print(x.upper())

print(x.capitalize())

print(x.swapcase()) #if lower means upper, upper means lower

print(x.center(8,' '))
# **QWERTY**
print(x.count('Q'))

print(x.find('W')) # found 1

print(x.find('Z')) # not found -1

print(x.index('E'))

s=("Sangavi","Bala")
print(" ".join(s))

data="   ABCD   --- ABCD  ---"
print(data.strip())
print(data.lstrip("-"))
print(data.rstrip("-"))
print(data.strip(" ")) #strip both left and right

print(x.split()) #list of substring

print(x.replace("Q","P"))

"""    6
    qwerty
    QWERTY
    Qwerty
    qwerty
    _QWERTY_
    1
    1
    -1
    2
    A-B-C-D
    ---ABCD   --- ABCD  ---
    ABCD   --- ABCD  ---
    ---ABCD   --- ABCD
    ABCD   --- ABCD
    ['QWERTY']
    PWERTY
"""
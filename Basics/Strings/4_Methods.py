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

max("what are you") # y 
# s1.__add__(s2) concatenate
# s.__getitem__(3) => char at index 3
# len(s) OR s.__len__()
# print("abc DEF".capitalize()) #Abc def

# print("abc. DEF".capitalize()) #Abc. def
# print("abcdef".center()) => expect atleast one argument
# print("abcdef".center(0)) => The entire string is printed when the argument passed to center() is less than the length of the string.
print("abcdef".center(7,"*")) # *abcdef
print("abcdef".center(8,"*")) # *abcdef*
# print("abcdef".center(7, 1)) # TypeError, the fill character must be a character, not an int.
print("xyyzxyzxzxyy".count('yy')) # 2
print("xyyzxyzxzxyy".count('yy', 2)) # 1
# print("xyyzxyzxzxyy".count('xyy', 0, 100)) # An error will not occur if the end value is greater than the length of the string itself.
print('abc'.encode()) # b’abc’
print("xyyzxyzxzxyy".endswith("xyy")) # True
print("ab\tcd\tef".expandtabs()) # Each \t is converted to 8 blank spaces by default.
print("ab\tcd\tef".expandtabs(4)) # Each \t is converted to 4 blank spaces.
print('{:,}'.format(1112223334)) # 1,112,223,334
#print('{:,}'.format('1112223334')) # Intiger is expected
#print('{:$}'.format(1112223334)) # Invalid
print('{:#}'.format(1112223334))  # 1112223334
print('{0:.2}'.format(1/3)) # 0.33
print('{0:.2%}'.format(1/3)) # 33.33%
print('ab12'.isalnum()) # True => Is Alphabetical and Numebr
print('ab'.isalpha()) # True
print('my_string'.isidentifier()) # True
print('a@ 1,'.islower()) # True
print('1.1'.isnumeric()) # The character . is not a numeric character.
print('HelloWorld'.istitle()) # True
print('1Rn@'.lower()) # 1rn@
print('xyyzxxyxyy'.lstrip('xyy')) # zxxyxyy
print('cba'.maketrans('abc', '123')) # {97: 49, 98: 50, 99: 51}
print('abcdef'.partition('cd')) # (‘ab’, ‘cd’, ‘ef’)
print('abcdefcdgh'.partition('cd')) # (‘ab’, ‘cd’, ‘efcdgh’)
print('abcd'.partition('cd')) # (‘ab’, ‘cd’, ”)
print('cd'.partition('cd')) # ('', 'cd', '')
print('abef'.partition('cd')) # ('abef', '', '')
print('abef'.replace('cd', '12')) # abef
print('abcdefcdghcd'.split('cd', 0)) # ['abcdefcdghcd']
print('abcdefcdghcd'.split('cd', -1)) # ['ab', 'ef', 'gh', '']
print('abcdefcdghcd'.split('cd', 2)) # [‘ab’, ‘ef’, ‘ghcd’] The string is split into a maximum of maxsplit+1 substrings.
print('ab\ncd\nef'.splitlines()) # [‘ab’, ‘cd’, ‘ef’]
print('ab cd ef'.title()) # Ab Cd Ef
print('ab cd-ef'.title()) # Ab Cd-Ef
print('ab'.zfill(5)) # 000ab




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
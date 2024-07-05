letters = "AaBbCcDd"

# Get all characters relying on default offsets
letters[::]
'AaBbCcDd'
letters[:]
'AaBbCcDd'

# Get every other character from 0 to the end
letters[::2]
'ABCD'

# Get every other character from 1 to the end
letters[1::2]
'abcd'

letters = "ABCDEF"

letters[::-1]
'FEDCBA'

letters
'ABCDEF'

letters = "ABCDEF"

letters[slice(None, None, -1)]
'FEDCBA'

greeting = reversed("Hello, World!")

next(greeting)
'!'
next(greeting)
'd'
next(greeting)
'l'

"".join(reversed("Hello, World!"))
'!dlroW ,olleH'

def reversed_string(text):
    result = ""
    for char in text:
        result = char + result
    return result


reversed_string("Hello, World!")
'!dlroW ,olleH'

from functools import reduce

def reversed_string(text):
    return reduce(lambda a, b: b + a, text)

reversed_string("Hello, World!")
'!dlroW ,olleH'

vowels = "eauoi"

"".join(sorted(vowels, reverse=True))
'uoiea'
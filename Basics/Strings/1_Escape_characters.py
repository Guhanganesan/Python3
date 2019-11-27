
"""
String
In computer programming, a string is traditionally a sequence of 
characters or  Strings are defined as an array of characters.
1. Escape Characters
2. Concatenation
3. Methods
4. Slicing
5. ASCII
6. Formatting
7. Looping
"""
x='a' 

print("\\")
print("\'")
print("\"he is my frnd\"")
#print("\a") #ASCII bell makes ringing the bell alert sounds
print("ab"+"\b")
print("Dear Friend,\f I am Python") #formfeed
print("Dear Friend, \n I am Python") #linefeed
print("apple")
print(' don\'t use this ')

print("He is going \tto my village")

print("c:myfolder\\docs\\files")

print("his\nname\nis")

#raw string

print(r"his\nname\nis")

x="""
      Dear frnd,
             I am Python.
             How are you
"""
print(x)

print("""
      <html>
            <bdoy>
               <h1> PYTHON</H2>
            </body>
      </html>
""")

print("A"*4)

print("A" "B") #concatenated

print("A"
      "B"
      "C")
"""
print("A"+"B")
a,b,c,d=10,20,30.05,"raja"
print(a,b,c,d) 
"""
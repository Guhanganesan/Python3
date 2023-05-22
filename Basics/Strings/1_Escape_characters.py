
"""
String
In computer programming, a string is traditionally a sequence of 
characters or  Strings are defined as an array of characters.
1. Escape Characters
	
      Character represented
      \a 	Alert (bell, alarm)
      \b 	Backspace
      \f 	Form feed (new page)
      \n 	New-line
      \r 	Carriage return
      \t 	Horizontal tab
      \v 	Vertical tab
      \' 	Single quotation mark
      \" 	Double quotation mark
      \? 	Question mark
      \\	Backslash 

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
#print("\a") # ASCII bell makes ringing the bell alert sounds
print("ab"+"\b")
print("Dear Friend,\f I am Python") #formfeed
print("Dear Friend, \n I am Python") #linefeed
print("apple")
print(' don\'t use this ')
"""
\
'
"he is my frnd"
ab
Dear Friend,
            I am Python
Dear Friend, 
 I am Python
apple
 don't use this 

"""

print("He is going \tto my village")

print("c:myfolder\\docs\\files")

print("his\nname\nis")

#raw string

print(r"his\nname\nis")
"""
He is going     to my village
c:myfolder\docs\files
his
name
is
his\nname\nis

"""

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
      
print("A"+"B")

print("A","B", 10) # print single line with different value

"""
AAAA
AB
ABC
AB
A B 10
"""
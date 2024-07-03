# Importing the StringIO module.
from io import StringIO 


# The arbitrary string.
string ='This is initial string.'

# Using the StringIO method to set
# as file object. Now we have an 
# object file that we will able to
# treat just like a file.
file = StringIO(string)

# this will read the file 
print(file.read())

# We can also write this file.
file.write(" Welcome to geeksforgeeks.")

# This will make the cursor at 
# index 0.
file.seek(0)

# This will print the file after 
# writing in the initial string.
print('The string after writing is:', file.read()) 

"""
This is initial string. 
The string after writing is: This is initial string. Welcome to geeksforgeeks.
"""

"""
StringIO.isatty():This function Return True if the stream is interactive and False if the stream not is interactive
StringIO.readable():This function return True if the file is readable and returns False if file is not readable.
StringIO.writable():This function return True if the file supports writing and returns False if file does not support writing.
StringIO.seekable():This function return True if the file supports random access and returns False if file does not support random access.
StringIO.closed:This function return True if the file is closed and returns False if file is open.

# Here the cursor is at index 0.
print(file.tell())
 
# Cursor is set to index 20.
file.seek(20)
 
# Print the index of cursor
print(file.tell())
"""
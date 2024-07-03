"""
Managing Resources using context manager: Suppose a block of code raises an exception or if it has a 
complex algorithm with multiple return paths, it becomes cumbersome to close a file in all the places. 
Generally in other languages when working with files try-except-finally is used to ensure that the file 
resource is closed after usage even if there is an exception. Python provides an easy way to manage resources: 
Context Managers. The with keyword is used. When it gets evaluated it should result in an object that performs
context management. Context managers can be written using classes or functions(with decorators).
"""
from contextlib import contextmanager
@contextmanager
def managed_file(name):
    try:
        file = open(name, 'w')
        yield file
    finally:
        file.close()
with managed_file('hello.txt') as f:
    f.write('hello, world! 2024')
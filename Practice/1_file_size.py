import os 
import math
path=r'D:\GithubRepositories\Python-2023\Python3\Basics\oop_notes.txt'
size = os.path.getsize(path)
print(size)

upper_limit = math.ceil(size/1024)

if upper_limit<1000:
    original_size = str(upper_limit)+" KB"
else:
    upper_limit = math.ceil(upper_limit/1000)
    original_size = str(upper_limit)+" MB"

print(original_size)


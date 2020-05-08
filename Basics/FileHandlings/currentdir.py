import os
print("get current working directory files")
path=os.getcwd()
#print(path)
dir=os.listdir(path) #[stores as list]
for i in dir:
	print(i)

"""
OR

import os
dir=os.listdir() #[stores as list]
for i in dir:
	print(i)
"""

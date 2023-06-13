import os
path="/"
dir=os.listdir(path) #[stores as list from starting]
print(dir)
for i in dir:
	print(i)

# Reference: https://docs.python.org/3/library/pathlib.html#pathlib.Path.unlink
# Referece: https://stackoverflow.com/questions/6996603/how-can-i-delete-a-file-or-folder-in-python

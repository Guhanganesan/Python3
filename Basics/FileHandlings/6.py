import os

directory = "MyFolder"

if directory:
    os.rmdir(directory) # Remove if already exist
  
parent_dir = os.getcwd()

path = os.path.join(parent_dir, directory)
  
os.mkdir(path)

print("Directory: ", directory)
print("Path: ", path)
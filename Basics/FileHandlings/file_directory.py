import os

directory = "MyFolder"

if directory:
    os.rmdir(directory) # Remove if already exist
  
# Base Dir
parent_dir = os.getcwd()

# Join
path = os.path.join(parent_dir, directory)

# Create
os.mkdir(path)

print("Directory: ", directory)
print("Path: ", path)
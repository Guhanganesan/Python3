import os 
relative_path_list = []
absolute_path_list = []
path="Test"
for dirpath, subdirs, files in os.walk(path):
    current_dir = dirpath
    base_dir = os.getcwd()
    full_path = os.path.join(base_dir, current_dir)
    for x in files:
        print(x)
        if x.endswith(".txt"):
            relative_path_list.append(os.path.join(dirpath, x))
            absolute_path_list.append(os.path.join(full_path, x))

print(relative_path_list)
print(absolute_path_list)

"""
test.txt
test.py
['Test\\test.txt']
['F:\\MyLearning\\Core_Python\\Python2020\\Basics\\FileHandlings\\Test\\test.txt']
"""

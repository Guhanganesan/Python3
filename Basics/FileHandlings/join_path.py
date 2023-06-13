import os 
textfiles = []
path="Test"
for dirpath, subdirs, files in os.walk(path):
    current_dir = dirpath
    base_dir = os.getcwd()
    full_path = os.path.join(base_dir, current_dir)
    print("Absolute Path: ", full_path)

"""
Absolute Path:  F:\MyLearning\Core_Python\Python2020\Basics\FileHandlings\Test
Absolute Path:  F:\MyLearning\Core_Python\Python2020\Basics\FileHandlings\Test\my_folder

"""
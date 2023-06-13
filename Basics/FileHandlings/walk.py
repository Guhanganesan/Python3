import os 
textfiles = []
path="Test"
for dirpath, subdirs, files in os.walk(path):
    print("Directory Path: ", dirpath)
    base_dir = os.getcwd()
    print("Base Directory Path: ", base_dir)
    print("Sub Directory Path: ", subdirs)

"""
Directory Path:  Test
Base Directory Path:  F:\MyLearning\Core_Python\Python2020\Basics\FileHandlings
Sub Directory Path:  ['my_folder']
Directory Path:  Test\my_folder
Base Directory Path:  F:\MyLearning\Core_Python\Python2020\Basics\FileHandlings
Sub Directory Path:  []
"""
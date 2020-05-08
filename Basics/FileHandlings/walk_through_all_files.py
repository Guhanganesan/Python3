import os 
textfiles = []
path="Test"
for dirpath, subdirs, files in os.walk(path):
    for x in files:
        if x.endswith(".txt"):
            textfiles.append(os.path.join(dirpath, x))

print(textfiles)


"""
['Test\\hello.txt', 'Test\\welcome.txt', 'Test\\docs\\test.txt']
"""

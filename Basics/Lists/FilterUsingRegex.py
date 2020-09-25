import re
files = ['test1.py', 'test.py','test3.py', 'test2.py']
files = sorted(files)
for file in files:
    pattern = re.compile("test(.*).py")
    if pattern.match(file):
        print("A", file)
    else:
        print("B", file)

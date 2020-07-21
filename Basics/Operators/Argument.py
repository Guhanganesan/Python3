import argparse
parser = argparse.ArgumentParser()
parser.add_argument("x", help="Enter number 1")
parser.add_argument("y", help="Enter number 2")
args = parser.parse_args()
print(args.x+args.y)
"""
B:\Python2020-main\Basics\Operators>python Argument.py 10 20
1020
"""


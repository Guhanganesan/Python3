data1 = input("Enter Values")
print(data1)

""" In python raw_input was removed. You should be used input() rather than the raw input.
    There are nothing differences between input() and raw_input, but you should focus on input. 
    In Python 2.7, raw_input() returns a string, and input() tries to run the input as a Python expression."""

print(eval("3+5"))

#For morethan one input

x,y=input("Enter Values").split()
print(x+y)


from sys import stdin, stdout

print("Enter Number")
x=stdin.readline()

stdout.write(x)

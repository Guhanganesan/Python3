#ZeroDivisionError: division by zero

a=10
b=0
try:
    print(a/b)  #critical statement

#except Exception:
#    print("You cannot divide a number by zero")

except Exception as e:
    print("U cannot divide a number by zero",e)
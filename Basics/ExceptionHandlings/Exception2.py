#ZeroDivisionError: division by zero

a=10
b=0
try:
    print("Start")
    print(a/b)  
    print("End") #this will not run when the exception is thrown
except Exception as e:
    print("U cannot divide a number by zero bcz:", e)


#ZeroDivisionError: division by zero

a=10
b=0
try:
    print("Open")
    print(a/b)  
   
except Exception as e:
    print("U cannot divide a number by zero bcz:", e)
    print("Close") # hence, we are going to finally

#ZeroDivisionError: division by zero

a=10
b=0
try:
    print("Open")
    print(a/b)  
   
except Exception as e:
    print("U cannot divide a number by zero bcz:", e)
finally:  
  print("Close") #finally block will be executed if we get errors as well as if we don't get errors

  

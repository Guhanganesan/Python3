#a,b,c,d=10,20,30,40,50
#print(a,b,c,d) --> ValueError

try:
    user=int(input("Enter a value"))
    print(user)  #
   
except ValueError as e:
    print("Should not use alphabets")

finally:  
    print("Close") 


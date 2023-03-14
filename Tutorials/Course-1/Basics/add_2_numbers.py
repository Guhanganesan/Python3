"""
first = input("Enter 1st number") # "10" # console input (user input)
sec = input("Enter 2nd number") # "12"
print(type(first)) #str
print(type(sec))
sum = first+sec # "10"+"12" = "1012"
print(sum)
"""

"""
first = input("Enter 1st number") # "10" # console input (user input)
sec = input("Enter 2nd number") # "12"
sum = int(first)+int(sec) # "10"+"12" = "1012"
print(sum)
"""

first = int(input("Enter 1st number: ")) # int("12")
sec = int(input("Enter 2nd number: ")) 
sum =  first+sec 
print("Result: ", sum)

"""
wrong => string+int => 'Result'+100
right => string+string => 'Result'+'100' <= str(100) concat
"""








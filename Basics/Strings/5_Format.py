#Formatting string 
code=76767
print("Chennai code:'code'")
print('The chennai code is :'code'..')
print("The chennai code is:{}".format(code))
print("He has {}, {} note".format(10,"rupees"))
print("{1},{0},{2}".format(10,20,30))
name="raja"
print("his name is %s" %(name))
#similarly int - %d, float %f
name="Anbu"
age=26
print("His name is {0} and age is {1}".format(name,age))
print("His name is {name}".format(name="Guhan"))
"""
for i in range(1,11):
    print("{} x 8 = {}".format(i,(i*8)))
"""




# brightness_4
# Formatting of Integers 
String1 = "{0:b}".format(16) 
print("\nBinary representation of 16 is ") 
print(String1) 
  
# Formatting of Floats 
String1 = "{0:e}".format(165.6458) 
print("\nExponent representation of 165.6458 is ") 
print(String1) 
  
# Rounding off Integers 
String1 = "{0:.2f}".format(1/6) 
print("\none-sixth is : ") 
print(String1) 

# String alignment 
String1 = "|{:<10}|{:^10}|{:>10}|".format('Geeks','for','Geeks') 
print("\nLeft, center and right alignment with Formatting: ") 
print(String1) 

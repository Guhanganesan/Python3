"""
variable = values
name = 'Guhan'                  => string
initial = 'G'                   => character
email = 'guhan@gmail.com'       => string
age = 32                        => int 
mobile = 979181555              => long int 
addr = '2/230, north -street ....' => string
marks_in_per = 82.5             => float
but in python int, str, float 
"""
name='Guhan'
street = "2/230, north -street, tanjavur - dist, PIN- 32623"
marks = 83.5 #float

new_marks =  int(marks) # Type casting , changed into other types
print(new_marks)
print(type(new_marks))  #int 

check_type = type(marks)
print(check_type) # float

marks = 82.5 #float
new_marks = int(marks)
print(new_marks) #82

marks = 90
new_marks = float(marks)
print(new_marks) #90.0 

x='12'
y=12
print(x+y)

x='12' #string
k=int(x) #int(x) 12 => float(x) 12.0
y=12
print(k+y)

# str()

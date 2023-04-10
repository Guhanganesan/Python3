
# Print data type
print(type(5))
print(type(0))
print(type(-10))
print(type(1_00_000))


num = 1,00,000
print(num)
print(type(num)) # (1, 0, 0)

value = 65
print(bin(value)) # Binary Format (Output would be 0b1000001)
print(oct(value)) # Octal Format (Output would be 0o101)
print(hex(value)) # Hexadecimal Format (Output would be 0x41)



# Convert Boolean to Integer
print('True', ":", int(True))
print('False', ":", int(False))

# Convert Floating Number to Integer
print('Float', ":", int(98.6))
print('Float', ":", int(1.0e4))

# Convert nondecimal integers
print('Binary', ":", int('10', 2))
print('Octal', ":", int('10', 8))
print('Hexadecimal', ":", int('10', 16))


mystring = '10'
print(type(mystring))
print(int(mystring), ":", type(int(mystring)))


float1 = 10e0
float2 = 5e1
float3 = 5.0e1

print(float1, "-", type(float1))
print(float2, "-", type(float2))
print(float3, "-", type(float3))

int1 = 10
int2 = -10
str1 = '20'

print('Boolean(True)', "-", float(True))
print('Boolean(False)', "-", float(False))
print('int1 - ', float(int1), type(float(int1)))
print('int2 - ', float(int2), type(float(int2)))
print('str1 - ', float(str1), type(float(str1)))


val = complex(2, 4)
print(val.real)
print(val.imag)
print(val.conjugate())

# Reference: https://www.golinuxcloud.com/python-numbers/


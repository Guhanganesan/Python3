import numpy as np 
print(np.pi)
print(np.sin(90))
val=(np.pi/180)*90
print(np.sin(val))

sinval=np.sin(val)
inv=np.arcsin(sinval)
deg=np.degrees(inv)
print(deg)

print(np.around(23.6778))
print(np.around(23.6778,1))
print(np.around(23.6778,-1))
print(np.around(23.6778,2))

print(np.floor(25.7889))
print(np.ceil(25.7889))

print(np.add(10,20))
print(np.subtract(10,20))
print(np.multiply(10,20))
print(np.divide(10,20))

print(np.power(10,2))
print(np.mod(11,2))

print(np.real(11+6j))
print(np.imag(11-6j))
print(np.conj(11+2j))
print(np.angle(11+2j))
print(np.angle(11+2j, deg=True))

print(np.amax(39,56))













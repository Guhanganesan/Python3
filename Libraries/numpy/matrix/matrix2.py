import numpy as np

A=np.ones((5,3))
#print(A)

B=5.0*np.ones((5,3))
#print(B)


C=np.random.randint(-5,5,(5,3))
#print(C)

D= np.multiply(A,B)
#print(D)

E=C**B
#print(E)

A+=B
A-=B
A*=B
A/=B
#print(A)

F=np.sqrt(B)
#print(F)

G=np.exp(B)
#print(G)

I=np.identity(5)
#print(I)


H=B.T 
#print(H)

C=np.array(
[
   [3,2,1],
   [6,2,7],
   [4,1,2]
])

Cinv=np.linalg.inv(C)
#print(Cinv)

I=np.dot(Cinv,C)
#print(I)


eigval, eigvec=np.linalg.eig(C)
#print(eigval)
print(eigvec)

#https://www.youtube.com/watch?v=Th0gnv9Ls3M&list=PLZ7s-Z1aAtmIRpnGQGMTvV3AGdDK37d2b



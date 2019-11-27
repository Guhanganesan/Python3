A = [[1,2,3], [1,2,3], [1,2,3]] 
B = [[1,2,3], [1,2,3], [1,2,3]] 
  
res = [[0 for x in range(3)] for y in range(3)]  

for i in range(len(A)): 
    for j in range(len(B[0])): 
        for k in range(len(B)):  
            res[i][j] += A[i][k] * B[k][j] 
  
print (res) 

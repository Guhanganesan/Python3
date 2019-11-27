A=[[1,2,3],[1,2,3],[1,2,3]]

B=[[1,2,3],[1,2,3],[1,2,3]]

S = [[0 for x in range(3)] for y in range(3)]
for i in range(0,len(B)):
    for j in range(0,len(B)):
        for k in range(0,len(B)):
            S[i][j]=S[i][j]+(A[i][k]*B[k][j])

for i in range(0, len(A)):
    for j in range(j, len(B)):
        print(S[i][j])



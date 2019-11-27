A=[[1,2,3],[1,2,3],[1,2,3]]
for i in range(0,len(A)):
    for j in range(0,len(A)):
        print(A[i][j],end=" ")
    print(" ")
print("-------------------------------")
B=[[1,2,3],[1,2,3],[1,2,3]]
for i in range(0,len(B)):
    for j in range(0,len(B)):
        print(B[i][j],end=" ")
    print(" ")

S=[[None,None,None],[None,None,None],[None,None,None]]

for i in range(0,len(B)):
    for j in range(0,len(B)):
        S[i][j]=A[i][j]+B[i][j]

print("--------------------------")

for i in range(0,len(B)):
    for j in range(0,len(B)):
        print(S[i][j], end=" ")
    print(" ")


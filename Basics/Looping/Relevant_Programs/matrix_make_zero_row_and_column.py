#make row and column as zero if found as zero 
data = [
    [1,2,3,0],
    [4,1,2,3],
    [5,1,0,5]
    ]
temp=[]

for i in range(0, len(data)):
    for j in range(0, len(data[0])):
        if data[i][j] == 0:
            temp.append([i,j])
            
for location_list in temp:
    for i in range(0, len(data)):
        for j in range(0,len(data[0])):
            if i == location_list[0]:
                data[i][j] = 0
            if j == location_list[1]:
                data[i][j] = 0
                
print(data)
            
"""
[[0, 0, 0, 0], [4, 1, 0, 0], [0, 0, 0, 0]]
"""

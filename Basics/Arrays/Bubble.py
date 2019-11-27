def bubbleSort(nlist):
    for i in range(len(nlist)-1,0,-1):
        for j in range(i):
            if nlist[j]>nlist[j+1]:
                temp = nlist[j]
                nlist[j] = nlist[j+1]
                nlist[j+1] = temp

nlist = [14,46,43,27,57,41,45,21,70]
bubbleSort(nlist)
print(nlist)

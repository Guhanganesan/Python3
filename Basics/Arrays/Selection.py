def selectionSort(nlist):
   for i in range(len(nlist)-1,0,-1):
       maxpos=0
       for j in range(1,i+1):
           if nlist[j]>nlist[maxpos]:
               maxpos = j

       temp = nlist[i]
       nlist[i] = nlist[maxpos]
       nlist[maxpos] = temp

nlist = [14,46,43,27,57,41,45,21,70]
selectionSort(nlist)
print(nlist)


L=[2,4,5,6,8,10,12]
search=4
left=0
right=len(L)-1
found=False
while left<=right and not found:
    mid=(left+right)//2
    if search==L[mid]:
        found=True
    else:
        if search<L[mid]:
            right=mid-1
        else:
            left=mid+1
if(found==True):
    print("Found")
else:
    print("Not Found")


def binarySearch(alist,item):
    left=0
    right=len(alist)-1
    found=False
    while left<=right and not found:
        mid=(left+right)//2
        if item==alist[mid]:
            found=True
        else:
            if item<alist[mid]:
                right=mid-1
            else:
                left=mid+1
    return found

print(binarySearch([2,4,5,6,8,10,12],5))

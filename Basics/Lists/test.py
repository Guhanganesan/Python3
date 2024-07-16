L=[2,5,7,8,12,14,15]
search=12
start=0
end=len(L)-1
while(start<=end):
    check=False
    mid=len(L)//2
    if(search==L[mid]):
        check=True
    elif(search<L[mid]):
        end=mid-1
        if(search==L[start]):
            check=True
    elif(search>L[mid]):
        start=mid+1
        if(search==L[start]):
            check=True
    
    start+=1
    
if(check==True):
    print("Found")
else:
    print("Not Found")

"""
a=[1,2,3]
b=[3,4,5]
c=[6,7,8]
# Output
# [(1, 3, 6), (2, 4, 7), (3, 5, 8)]
"""

"""
x = "578"
y = atoi(x)
type(x) # str
type(y) # int

"""
s="578" # [48, 49, 50, 51,52,53,54,55,56,57,57]
def atoi(s):
    L=list(s) #['5','7','8']
    L=[ord(char) for char in L]
    print(L)
    temp=0
    for index in range(0,len(L)):
        if index == 0:
            temp=temp+ (L[index] - ord('0'))*100
        if index == 1:
            temp=temp+(L[index] - ord('0'))*10
        if index == 2:
            temp=temp+(L[index] - ord('0'))*1
    return temp
   
res = atoi(s)
print(res)

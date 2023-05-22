L=[5,1,3,6,8,7,2]
f=0
s=0 # 2nd largest stored at 2nd place ans: 8, 7
"""
5>0
s=0    f=5  wrong f=L[i]
f=5    s=0        s=f 
    
1>5 
3>5
6>5 
s=5
f=6

8>6
s=6
f=8

7>8    or 7>6 
            s=7

"""
for i in range(0,len(L)):
    if(L[i]>f): #5>0
        s=f
        f=L[i]
    elif(L[i]>s):
        s=L[i]
        
print(f,s)

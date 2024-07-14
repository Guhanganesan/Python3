"""
sum of square of digits which is less than 10 in a list
"""
my_list=[]

def sum_of_digits(sq):
   
    num = sq
    temp=0
    while(num>0):
        rem= num%10 
        temp=temp+rem
        num = num//10 
        
    if temp < 10:
        my_list.append(sq)
    

for i in range(1, 40):
    
    sq = i*i  
   
    sum_ = sum_of_digits(sq)
    
        
print(my_list)
        
    
# res: [1, 4, 9, 16, 25, 36, 81, 100, 121, 144, 225, 324, 400, 441, 900, 1024, 1521]

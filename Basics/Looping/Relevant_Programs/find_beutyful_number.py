def find_range(start, end):
    if start>end:
        return end - start
    else:
        return 1 

start=int(input("Enter starting number"))
end=int(input("Enter ending number"))
if start > end:
    start, end = end, start

size = find_range(start, end)

def find_sum_of_square(num):
    temp=0
    while num != 0:
        temp = temp +(num % 10 * num % 10) 
        num = num // 10
    print("sum of square: ", temp)
    return temp


beuty_sum=0 

for num in range(start, end+1):
    print("given num is: ", num)
    ss_num = find_sum_of_square(num)
    
    if ss_num == 1:
        print("beutyful number is: ", num)
        beuty_sum = beuty_sum + num
    else:
        while ss_num > 9:
            ss_num = find_sum_of_square(ss_num)
            if ss_num == 1:
                print("beutyful number is: ", num)
                beuty_sum = beuty_sum + num
                
    
    
print("beuty_sum: ", beuty_sum)
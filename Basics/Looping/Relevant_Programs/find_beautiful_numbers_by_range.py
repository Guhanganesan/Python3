def find_range(start, end):
    if start>end:
        return end - start
    else:
        return 1 
        
def find_sum_of_square(num):
        temp=0
        while num > 0:
            rem = (num % 10)
            temp = temp+rem**2
            num = num // 10
        return temp
        
List = []
ranging = int(input("Enter how many range"))
for index in range(1, ranging+1):
    print("Enter Rage ",index)
    number1=int(input("Enter starting number: "))
    number2=int(input("Enter ending number: "))
    List.append([number1,number2]) 
    
print(List)


        
for sub_list in List:
    start = sub_list[0]
    end = sub_list[1]
    if start > end:
        start, end = end, start
    
    size = find_range(start, end)
    
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
                print("sum of square: ", ss_num)
                if ss_num == 1:
                    print("beutyful number is: ", num)
                    beuty_sum = beuty_sum + num
    
    print("beuty_sum for range",sub_list, " ", beuty_sum)

"""
Enter how many range3
Enter Rage  1
Enter starting number: 2
Enter ending number: 3
Enter Rage  2
Enter starting number: 4
Enter ending number: 8
Enter Rage  3
Enter starting number: 31
Enter ending number: 33
[[2, 3], [4, 8], [31, 33]]
given num is:  2
given num is:  3
beuty_sum for range [2, 3]   0
given num is:  4
sum of square:  37
sum of square:  58
sum of square:  89
sum of square:  145
sum of square:  42
sum of square:  20
sum of square:  4
given num is:  5
sum of square:  29
sum of square:  85
sum of square:  89
sum of square:  145
sum of square:  42
sum of square:  20
sum of square:  4
given num is:  6
sum of square:  45
sum of square:  41
sum of square:  17
sum of square:  50
sum of square:  25
sum of square:  29
sum of square:  85
sum of square:  89
sum of square:  145
sum of square:  42
sum of square:  20
sum of square:  4
given num is:  7
sum of square:  97
sum of square:  130
sum of square:  10
sum of square:  1
beutyful number is:  7
given num is:  8
sum of square:  52
sum of square:  29
sum of square:  85
sum of square:  89
sum of square:  145
sum of square:  42
sum of square:  20
sum of square:  4
beuty_sum for range [4, 8]   7
given num is:  31
sum of square:  1
beutyful number is:  31
given num is:  32
sum of square:  10
sum of square:  1
beutyful number is:  32
given num is:  33
sum of square:  65
sum of square:  61
sum of square:  37
sum of square:  58
sum of square:  89
sum of square:  145
sum of square:  42
sum of square:  20
sum of square:  4
beuty_sum for range [31, 33]   63
"""

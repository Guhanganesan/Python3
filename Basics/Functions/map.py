#map(funtion, iteration)
def sum_of_digits_of_squares(num):
    temp = 0
    while num != 0:
        rem = num % 10
        temp = temp + rem * rem
        num = num//10
    return temp

numbers = (11, 12, 13, 24, 25)
result = list(map(sum_of_digits_of_squares, numbers))
print(result)
#filter(funtion, iteration)
def filter_number(num):
    return num>15

numbers = (11, 12, 13, 24, 25)
result = list(filter(filter_number, numbers))
print(result)
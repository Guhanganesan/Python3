
# Example filtering objects based on attribute
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
people = [
    Person('Alice', 25),
    Person('Bob', 30),
    Person('Charlie', 22)
]
# Filter people older than 25
filtered_people = list(filter(lambda person: person.age > 25, people))
for person in filtered_people:
    print(person.name, person.age)


# Define a function to check 
# if a number is a multiple of 3
def is_multiple_of_3(num):
    return num % 3 == 0

# Create a list of numbers to filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter and a lambda function to
# filter the list of numbers and only
# keep the ones that are multiples of 3
result = list(filter(lambda x: is_multiple_of_3(x), numbers))

# Print the result
print(result) # [3, 6, 9]

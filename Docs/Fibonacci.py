"""
The Fibonacci series is a sequence where each number is the sum of the two preceding ones, 
starting from 0 and 1. The series typically starts as 0, 1, 1, 2, 3, 5, 8, 13, and so on...
"""

# Example 1
def fibonacci_iterative(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example usage
n = int(input("Enter the number of Fibonacci numbers to generate: "))
print(f"Fibonacci sequence (iterative): {fibonacci_iterative(n)}")


# Example 2

"""
Generator Approach: Useful for generating Fibonacci numbers one at a time, 
especially when dealing with a very large sequence.
"""

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Example usage
n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_gen = fibonacci_generator()
sequence = [next(fib_gen) for x in range(n)]
print(f"Fibonacci sequence (generator): {sequence}")


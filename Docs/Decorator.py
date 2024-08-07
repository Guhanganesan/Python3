"""
Certainly! A Python decorator is a design pattern that allows you to add behavior to functions or methods without modifying their code. 
Decorators are often used to add functionality like logging, access control, or timing to functions.
"""
# Example 1

import time

# Decorator function
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record end time
        elapsed_time = end_time - start_time
        print(f"Function {func.__name__} took {elapsed_time:.4f} seconds to execute.")
        return result
    return wrapper

# Use the decorator
@timing_decorator
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

# Call the decorated function
result = example_function(1000000)
print(f"Result: {result}")

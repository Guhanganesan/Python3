def prime_factors(n):
    factors = []
    # Divide by 2 until n is no longer divisible by 2
    while n % 2 == 0:
        factors.append(2) #2,2
        n = n // 2 #10,5
    
    # Divide by odd numbers from 3 up to sqrt(n)
    divisor = 3
    while divisor * divisor <= n: #9<25
        while n % divisor == 0:
            print(n)
            factors.append(divisor)
            n = n // divisor
        divisor += 2
    
    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    
    return factors

# Example usage
number = int(input("Enter a number to find its prime factors: "))
print(f"Prime factors of {number}: {prime_factors(number)}")
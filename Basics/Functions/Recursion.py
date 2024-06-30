def fact(n): 
    if (n == 0): 
        return 1
    return n * fact(n-1) 
   
# print the result
print(fact(5)) #120 

x = list(map(fact,[5]))
print(x) #[120]


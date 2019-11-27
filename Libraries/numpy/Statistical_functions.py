import numpy as np
normal_array = np.random.normal(5, 0.5, 6) #ValueError: scale < 0
print(normal_array)	

print(np.min(normal_array))

print(np.max(normal_array))

print(np.mean(normal_array))

print(np.median(normal_array))

print(np.std(normal_array))




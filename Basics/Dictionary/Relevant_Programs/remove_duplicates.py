# Remove duplicates from dictionary
# duplicate keys never allows values allowed
data = {'D': 'red', 'B': 'green', 'A': 'yellow','E':'green','G': 'orange','R':'red'}
print(data)

result = {}

for key, value in data.items():
    if value not in result.values(): # 'a' in ['a','b']
        result[key]=value

print(result)



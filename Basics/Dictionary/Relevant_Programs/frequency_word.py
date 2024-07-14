# Frequency of word
user_data = input("Enter a String: ") # Hello guhan ganesan
user_data_list = user_data.split()
print(user_data_list) # ['Hello', 'guhan', 'ganesan']

word_freq = {}
for item in user_data_list:
    if item in user_data_list:
        word_freq[item]=user_data_list.count(item)

print(word_freq)

"""
Enter a String: hello guhan ganesan hello how are you guhan
['hello', 'guhan', 'ganesan', 'hello', 'how', 'are', 'you', 'guhan']
{'hello': 2, 'guhan': 2, 'ganesan': 1, 'how': 1, 'are': 1, 'you': 1}
""" 


import re

def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    # Compare the string with its reverse
    print(s)
    return s == s[::-1]

# Example usage
if __name__ == "__main__":
    user_input = input("Enter a string to check if it's a palindrome: ")
    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome.")
    else:
        print(f"'{user_input}' is not a palindrome.")

"""
Remove spaces and convert to lowercase
s = s.replace(" ", "").lower()
"""
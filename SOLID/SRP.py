"""
Single Responsibility Principle (SRP)
The Single Responsibility Principle states that a class should have only one reason to change. 
Each class should handle a single part of the functionality.
"""

# SRP: User class only handles user-related data
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

# SRP: AuthenticationService class handles authentication
class AuthenticationService:
    def __init__(self):
        self.users = []

    def register_user(self, user):
        self.users.append(user)

    def authenticate(self, username, email):
        for user in self.users:
            if user.username == username and user.email == email:
                return True
        return False

# Creating a user and using the authentication service
user = User("john_doe", "john@example.com")
auth_service = AuthenticationService()
auth_service.register_user(user)
print(auth_service.authenticate("john_doe", "john@example.com"))  # Output: True
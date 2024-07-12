"""
The Dependency Inversion Principle states that high-level modules should 
not depend on low-level modules but on abstractions.
"""
from abc import ABC, abstractmethod

# DIP: Abstract interface for Notification
class NotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass

# DIP: High-level module depends on abstraction
class UserNotifier:
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def notify_user(self, message):
        self.notification_service.send(message)

# DIP: Low-level modules implementing the abstraction
class EmailService(NotificationService):
    def send(self, message):
        print(f"Sending email with message: {message}")

class SMSService(NotificationService):
    def send(self, message):
        print(f"Sending SMS with message: {message}")

# Using the notifier with different services
email_service = EmailService()
sms_service = SMSService()

notifier = UserNotifier(email_service)
notifier.notify_user("Hello via Email")

notifier = UserNotifier(sms_service)
notifier.notify_user("Hello via SMS")

"""
These examples illustrate how adhering to SOLID principles in Python helps create more maintainable, 
scalable, and flexible software designs. Each principle addresses a specific aspect of code structure 
and design, contributing to overall code quality.
"""

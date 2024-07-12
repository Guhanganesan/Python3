"""
The Open/Closed Principle states that software entities should be open for extension 
but closed for modification.
"""
# OCP: Base class for Payment processing
class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses should implement this method")

# OCP: Extending functionality without modifying base class
class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}")

class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount}")

# Using the payment processors
payment_methods = [CreditCardPayment(), PayPalPayment()]
for method in payment_methods:
    method.process_payment(100)
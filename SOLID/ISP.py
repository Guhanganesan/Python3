"""
he Interface Segregation Principle states that no client should be forced to depend on methods 
it does not use.
"""
from abc import ABC, abstractmethod

# ISP: Separate interfaces for Printer and Scanner
class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

# ISP: Implementing only the required interfaces
class MultiFunctionPrinter(Printer, Scanner):
    def print_document(self, document):
        print(f"Printing: {document}")

    def scan_document(self):
        print("Scanning document")

class SimplePrinter(Printer):
    def print_document(self, document):
        print(f"Printing: {document}")

# Using the printers
mfp = MultiFunctionPrinter()
mfp.print_document("SOLID Principles")
mfp.scan_document()

sp = SimplePrinter()
sp.print_document("SOLID Principles")
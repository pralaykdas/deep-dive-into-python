# Interface-Segregation Principle (ISP)

"""
“Clients should not be forced to depend on methods they do not use.”

# The principle states that the clients should not be forced to depend on the methods or implement the interfaces that they do not use. Interfaces belong to clients, not to hierarchies.
# Purpose:
    * Design fine-grained interfaces that are client-specific
"""


# Problem
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

    def fax(self, document):
        raise NotImplementedError("Fax functionality not supported")

    def scan(self, document):
        raise NotImplementedError("Scan functionality not supported")

class ModernPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")

"""
Why it violates ISP?
OldPrinter only supports printing — but it’s forced to implement fax() and scan(), which it doesn't support.

These unused methods throw NotImplementedError, which:
    * Violates interface expectations
    * Causes code bloat, confusion, and potential runtime errors

This tightly couples unrelated functionalities in one interface.
"""


# Solution
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

class NewPrinter(Printer, Fax, Scanner):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")

"""
How It Follows ISP?
Interfaces are split into smaller, focused ones:
    * Printer for printing
    * Fax for faxing
    
Scanner for scanning:
    * OldPrinter only implements what it actually supports — the Printer interface
    * NewPrinter supports all features and opt-in implements all relevant interfaces

This design is:
    * Cleaner
    * More modular
    * Easier to maintain and test
"""

# Liskov-Substitution Principle (LSP)

"""
“Objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.”

# The principle states that a child class must be substitutable for its parent class.
# Purpose:
#     * Ensure that a child class can assume the place of its parent class without causing any errors.
"""


# Problem
class Pizza:
    def __init__(self, size):
        self.size = size
    
    def calculate_price(self):
        # Calculate price based on size
        pass

class SpecialPizza(Pizza):
    def calculate_price(self):
        # Calculate special price logic
        pass

"""
What’s the Issue?
While SpecialPizza inherits from Pizza, it might not behave exactly like a Pizza due to different pricing logic, especially if it introduces side effects, changes assumptions, or needs extra parameters like special_instructions.

For example:

If some client code expects Pizza.calculate_price() to behave a certain way, replacing it with SpecialPizza may break the logic because it behaves differently.

SpecialPizza might need more data (special_instructions) to work properly, but the base class Pizza knows nothing about this requirement.


Why this violates LSP?
Substituting Pizza with SpecialPizza breaks expectations because:

-> The method interface and internal logic no longer align perfectly.

-> The subclass relies on behaviors or data not present in the superclass.

This weakens the inheritance contract.
"""


# Solution
from abc import ABC, abstractmethod

class FoodItem(ABC):
    @abstractmethod
    def calculate_price(self):
        pass

class Pizza(FoodItem):
    def __init__(self, size):
        self.size = size
    
    def calculate_price(self):
        # Calculate price based on size
        pass

class SpecialPizza(FoodItem):
    def __init__(self, size, special_instructions):
        self.size = size
        self.special_instructions = special_instructions
    
    def calculate_price(self):
        # Calculate special price logic
        pass

"""
How this fixes the problem?
-> Common interface: Both Pizza and SpecialPizza implement FoodItem. They are no longer in a parent-child relationship, but siblings with a shared contract.

-> Independent behavior: Each class implements its own calculate_price() logic without having to conform to the constraints of the other.

-> LSP compliant: Wherever a FoodItem is expected, either Pizza or SpecialPizza can be used without breaking the code’s logic.
"""

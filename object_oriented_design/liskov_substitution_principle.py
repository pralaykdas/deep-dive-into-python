# Liskov-Substitution Principle
# The principle states that a child class must be substitutable for its parent class.
# The purpose is to ensure that the child class can assume the place of its parent class without causing any errors.


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

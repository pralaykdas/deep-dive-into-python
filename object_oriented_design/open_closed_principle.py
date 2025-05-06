# Open-Closed Principle (OCP)

"""
“Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification.”

# The principle states that the software entities should be open for extension, but closed for modification.
# The purpose is to make it easier to add new features to the system, without directly modifying the existing code.
# Purpose:
    * Make the code easier to add new features to the system, without directly modifying the existing code.
"""


# Problem
from math import pi

class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if self.shape_type == "rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]
        elif self.shape_type == "circle":
            self.radius = kwargs["radius"]

    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "circle":
            return pi * self.radius**2

rectangle = Shape("rectangle", width=10, height=5)
rectangle.calculate_area()
circle = Shape("circle", radius=5)
circle.calculate_area()

"""
Why it violates OCP?
Adding a new shape like Square requires modifying the Shape class:

-> Add new shape logic in __init__

-> Add new case in calculate_area

Every new shape adds more if/elif statements, which:

-> Bloats the class

-> Makes it more fragile (existing logic might break)

-> Breaks OCP — you're modifying a stable class repeatedly
"""


# Solution
from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def calculate_area(self):
        return self.side**2

"""
How it follows OCP?
-> You can add new shapes (like Triangle, Ellipse, etc.) by creating new subclasses — no need to touch existing Shape, Circle, or Rectangle classes.

-> Each shape’s logic is encapsulated and self-contained.

-> The base class Shape is closed for modification, but open for extension via inheritance.
"""

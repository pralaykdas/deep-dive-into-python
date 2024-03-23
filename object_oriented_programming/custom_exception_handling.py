# Exception handling - Raise and custom

class ExceptionHandling:
    celcius_value = 10

    # Raise exception method
    def raise_exception(self, a, b):
        try:
            raise TypeError("The values are not of the same type", a, b)
        except TypeError as e:
            print(e.args)

    # Re-raise an exception method
    def re_raise_exception(self, a ,b):
        try:
            return a/b
        except ZeroDivisionError as e:
            print(e)
            raise ValueError("The values for b argument cannot be zero.")
    
    # Custom exception method
    def custom_exception(self):
        if not (self.celcius_value >= 30 and self.celcius_value <= 100):
            raise CelciusError(10)

class CelciusError(Exception):
    # Class attributes
    min_c = 30
    max_c = 100
    
    # Instance attributes
    def __init__(self, celcius: int, *args: object) -> None:
        super().__init__(*args)
        self.celcius = celcius

    # __str__ method call
    def __str__(self) -> str:
        return "The temperature {} is not in range between {}-{}".format(self.celcius, self.min_c, self.max_c)


# Raise exception
# Object creation
obj_1 = ExceptionHandling()
# obj_1.raise_exception(2, 3)
# obj_1.re_raise_exception(10, 0)

# Custom exception
# Disable the above calls to activate the custom exception call
obj_1.custom_exception()

# Output for raise exception method call
"""
('The values are not of the same type', 2, 3)
division by zero
Traceback (most recent call last):
  File "<file-path>\deep-dive-into-python\object_oriented_programming\exception_handling_2.py", line 16, in re_raise_exception
    return a/b
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<file-path>\deep-dive-into-python\object_oriented_programming\exception_handling_2.py", line 44, in <module>
    obj_1.re_raise_exception(10, 0)
  File "<file-path>\deep-dive-into-python\object_oriented_programming\exception_handling_2.py", line 19, in re_raise_exception
    raise ValueError("The values for b argument cannot be zero.")
ValueError: The values for b argument cannot be zero.
"""

# Output for custom exception method call
"""
Traceback (most recent call last):
  File "<file-path>\deep-dive-into-python\object_oriented_programming\exception_handling_2.py", line 48, in <module>
    obj_1.custom_exception()
  File "<file-path>\deep-dive-into-python\object_oriented_programming\exception_handling_2.py", line 24, in custom_exception
    raise CelciusError(10)
__main__.CelciusError: The temperature 10 is not in range between 30-100
"""
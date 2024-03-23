# Exception handling

import sys

class ExceptionHandling:
    # Class attributes
    num_list = [1, 2, 3, 4, 5]

    # Instance attributes
    def __init__(self, a: int, b:int) -> None:
        self.a = a
        self.b = b

    # Update values method
    def set_value(self, a, b):
        self.a = a
        self.b = b

    # Index error method
    def index_error_exception(self) -> None:
        try:
            print(self.num_list[6])
        except IndexError as e:
            print("Exception occurred: {}".format(e.__class__))

    # Type error method
    def type_error_exception(self) -> None:
        try:
            print (self.a/self.b)
        except TypeError as e:
            print("Exception occurred: {}".format(e.__class__))

    # Zero division error method
    def zero_division_error_exception(self) -> None:
        try:
            print (self.a/self.b)
        except ZeroDivisionError as e:
            print("Exception occurred: {}".format(e.__class__))

    # Base error method
    def base_exception(self) -> None:
        try:
            print (self.a/self.b)
            print(self.num_list[6])
        except (IndexError, TypeError, ZeroDivisionError, Exception) as e:
            print("Exception occurred: {}".format(e.__class__))

    # Identify exception method
    def identify_exception(self) -> None:
        try:
            print (self.a/self.b)
        except:
            exec_info = sys.exc_info()
            print(exec_info)
            print("Exception Type: {}\nException value: {}\nTraceback: {}".format(exec_info[0], exec_info[1], exec_info[2]))


# Object 1
obj_1 = ExceptionHandling(1, "a")
# Check Type error
obj_1.type_error_exception()
# Check Index error
obj_1.index_error_exception()
# Object 2
obj_2 = ExceptionHandling(1, 0)
# Check Zero Division error
obj_2.zero_division_error_exception()
# Check Base error
obj_1.base_exception()
# Update values
obj_1.set_value(1, 2)
# Check Type error
obj_1.base_exception()
# Check Index error
obj_2.base_exception()
# Identify exception
obj_2.identify_exception()

# Output
"""
Exception occurred: <class 'TypeError'>
Exception occurred: <class 'IndexError'>
Exception occurred: <class 'ZeroDivisionError'>
Exception occurred: <class 'TypeError'>
0.5
Exception occurred: <class 'IndexError'>
Exception occurred: <class 'ZeroDivisionError'>
(<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero'), <traceback object at 0x000001AEA2973DC0>)
Exception Type: <class 'ZeroDivisionError'>
Exception value: division by zero
Traceback: <traceback object at 0x000001AEA2973DC0>
"""
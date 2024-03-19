# Classes and Objects

class Person:
    # Class attributes
    object_counter = 0
    
    # Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.object_counter += 1

    # Instance methods
    def greet(self):
        return "Hi {}".format(self.name)

    # Class methods
    @classmethod
    def create_anonymous(cls):
        return Person("Anonymous", 42)

    # Static methods
    @staticmethod
    def display_name(name: str):
        return "My name is: {}".format(name)


class Employee(Person):
    # Instance attributes
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title

    # Instance methods
    def greet(self):
        return super().greet()


# Object 1
person_1 = Person("Alpha", "30")
print("Name: {}\nAge: {}".format(person_1.name, person_1.age))
print(person_1.greet())

# Object 2
person_2 = Person("Beta", "25")
print("Name: {}\nAge: {}".format(person_2.name, person_2.age))
print(person_2.greet())

# Object counter call
print("Object counter: {}".format(Person.object_counter))

# Class method call
anonymous = Person.create_anonymous()
print("Anonymous name: {}".format(anonymous.name))

# Static method call
print(Person.display_name("Tango"))

# Single inheritance
employee_1 = Employee("Delta", 28, "Python Developer")
print("Name: {}\nAge: {}\nJob title: {}".format(employee_1.name, employee_1.age, employee_1.job_title))
print(employee_1.greet())


# Output
"""
Name: Alpha
Age: 30
Hi Alpha
Name: Beta
Age: 25
Hi Beta
Object counter: 2
Anonymous name: Anonymous
My name is: Tango
Name: Delta
Age: 28
Job title: Python Developer
Hi Delta
"""
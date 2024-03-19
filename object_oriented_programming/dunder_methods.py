# Dunder methods

class Person:
    # Instance attributes
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    # __str__ method
    def __str__(self) -> str:
        return "Name: {}\nAge: {}".format(self.name, self.age)
    
    # The __str__ calls __repr__ internally by default.
    # __repr__ method
    def __repr__(self) -> str:
        return "Name: {}\nAge: {}".format(self.name, self.age)
    
    # __eq__ method
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Person):
            return self.age == __value.age
        return False
    
    # If you implement __eq__, Python sets __hash__ to None unless you implement __hash__.
    # __hash__ method
    def __hash__(self) -> str:
        return hash(self.name)
     
    # __bool__ method
    def __bool__(self) -> bool:
        if self.age < 30:
            return False
        return True
    
    # If a class doesn’t implement the __bool__ method, Python will use the result of the __len__ method.
    # __len__ method
    def __len__(self) -> int:
        return len(self.name)
    
    # __del__ method
    def __del__(self) -> None:
        print("__del__ was called.")


# Object 1
person_1 = Person("Alpha", 30)
print("Name: {}\nAge: {}".format(person_1.name, person_1.age))

# Object 2
person_2 = Person("Beta", 25)
print("Name: {}\nAge: {}".format(person_2.name, person_2.age))

# Object 3
person_3 = Person("Delta", 25)
print("Name: {}\nAge: {}".format(person_3.name, person_3.age))

# __str__ method call
print(person_1)

# __repr__ method call
print(repr(person_2))

# __eq__ method call
print("Person 1 is equal to Person 2; {}".format(person_1 == person_2))
print("Person 2 is equal to Person 3; {}".format(person_2 == person_3))
print("Person 2 is equal to integer; {}".format(person_2 == 25))

# __hash__ method call
print("Hash value of Person 1 name: {}".format(hash(person_1)))

# __bool__ method call
print("Bool value for Person 1: {}".format(bool(person_1)))
print("Bool value for Person 2: {}".format(bool(person_2)))

# __len__ method call
person_3.name = ""
print("Length value for Person 1: {}".format(len(person_1)))
print("Bool value for Person 1: {}".format(bool(person_1)))
print("Bool value for Person 3: {}".format(bool(person_3)))

# __del__ method call
person_2 = None
del person_3
print("__del__ method call completed.")

# Output
"""
Name: Alpha
Age: 30
Name: Beta
Age: 25
Name: Delta
Age: 25
Name: Alpha
Age: 30
Name: Beta
Age: 25
Person 1 is equal to Person 2; False
Person 2 is equal to Person 3; True
Person 2 is equal to integer; False
Hash value of Person 1 name: 129452403774439646
Bool value for Person 1: True
Bool value for Person 2: False
Length value for Person 1: 5
Bool value for Person 1: True
Bool value for Person 3: False
__del__ was called.
__del__ was called.
__del__ method call completed.
__del__ was called.
"""
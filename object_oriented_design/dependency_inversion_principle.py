# Dependency-Inversion Principle (DIP)

"""
“High-level modules should not depend on low-level modules. Both should depend on abstractions.”

# The principle states that the high-level modules should not depend on the low-level modules. Both should depend on abstractions. The abstractions should not depend on the details. The details should depend on the abstractions.
# Purpose:
    * Reduce coupling between the classes by introducing an abstraction layer between them.
"""


# Problem
class FrontEnd:
    def __init__(self, back_end):
        self.back_end = back_end

    def display_data(self):
        data = self.back_end.get_data_from_database()
        print("Display data:", data)

class BackEnd:
    def get_data_from_database(self):
        return "Data from the database"

"""
Why it violates DIP?
The FrontEnd class directly depends on the concrete BackEnd class.

The method get_data_from_database() is specific to one implementation.

This makes the frontend:
    * Tightly coupled to the backend
    * Hard to test (you can’t easily mock or substitute the backend)
    * Inflexible (you must modify FrontEnd to switch to another data source like an API)
"""


# Solution
from abc import ABC, abstractmethod

class FrontEnd:
    def __init__(self, data_source):
        self.data_source = data_source

    def display_data(self):
        data = self.data_source.get_data()
        print("Display data:", data)

class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass

class Database(DataSource):
    def get_data(self):
        return "Data from the database"

class API(DataSource):
    def get_data(self):
        return "Data from the API"


db_front_end = FrontEnd(Database())
db_front_end.display_data()    # Display data: Data from the database


api_front_end = FrontEnd(API())
api_front_end.display_data()    # Display data: Data from the API

"""
How it follows DIP?
FrontEnd now depends on the abstraction DataSource, not on any specific backend class.

Database and API are low-level implementations of the DataSource interface.

You can easily:
    * Substitute a different data provider (e.g. MockSource, FileSource)
    * Test with mocks or stubs
    * Add new data sources without modifying FrontEnd
"""

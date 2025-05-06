# Single-Responsibility Principle (SRP)

"""
“A class should have only one reason to change.”

# The principle states that every class, function, and method should have only one job or one reason to change.
# Purpose:
    * Create highly cohesive and robust classes, methods, and functions
    * Promote class composition
    * Avoid code duplication
"""


# Problem
from pathlib import Path
from zipfile import ZipFile

class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()

"""
Why it violates SRP?
The class has multiple responsibilities:

-> File reading/writing

-> File compression/decompression

So it has multiple reasons to change:

-> If compression needs change (e.g. switch to .tar.gz)

-> If read/write behavior changes (e.g. encoding, logging)

This makes the class hard to maintain and test.
"""


# Solution
from pathlib import Path
from zipfile import ZipFile

class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

class ZipFileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()

"""
How it follows SRP?
-> FileManager is only responsible for file content management.

-> ZipFileManager is only responsible for file compression.

Now, each class has one reason to change, and you can evolve or test each independently.
"""

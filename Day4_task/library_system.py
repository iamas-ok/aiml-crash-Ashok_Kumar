# Task 05: Inheritance — Library System
# Builds a library system using OOP inheritance with a base class and two child classes.


class LibraryItem:
    """Base class representing a generic library item."""

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def describe(self) -> str:
        """Returns a basic description of the library item."""
        return f"'{self.title}' by {self.author} ({self.year})"


class Book(LibraryItem):
    """Child class representing a physical book with a page count."""

    def __init__(self, title: str, author: str, year: int, pages: int):
        super().__init__(title, author, year)   # inherit base attributes
        self.pages = pages

    def describe(self) -> str:
        """Overrides describe() to include page count."""
        return f"[BOOK]  {super().describe()} — {self.pages} pages"


class EBook(LibraryItem):
    """Child class representing a digital book with a file size."""

    def __init__(self, title: str, author: str, year: int, file_size_mb: float):
        super().__init__(title, author, year)   # inherit base attributes
        self.file_size_mb = file_size_mb

    def describe(self) -> str:
        """Overrides describe() to include file size in MB."""
        return f"[EBOOK] {super().describe()} — {self.file_size_mb} MB"


# Create 2 Book and 2 EBook objects
b1 = Book("The Ampire",         "piyush",    1988, 208)
b2 = Book("Atomic Habits",         "James Clear",     2018, 320)
e1 = EBook("Deep Work",            "Cal Newport",     2016, 4.5)
e2 = EBook("Python Crash Course",  "Eric Matthes",    2019, 12.3)

# Store all in one list and loop through
library = [b1, b2, e1, e2]

print("Library Catalogue-->>")
for item in library:
    print(item.describe())


# EXPLORE: isinstance()
print("\nisinstance() checks-->>")
print(f"Is b1 a Book?         {isinstance(b1, Book)}")           # True
print(f"Is b1 a LibraryItem?  {isinstance(b1, LibraryItem)}")    # True — because Book inherits from LibraryItem
print(f"Is b1 an EBook?       {isinstance(b1, EBook)}")          # False

# EXPLANATION:
# isinstance(b1, LibraryItem) returns True even though b1 was created as a Book.
# This is because Book is a subclass of LibraryItem — every Book IS-A LibraryItem.
# Python's isinstance() checks the entire inheritance chain, not just the immediate class.
# This is the core idea behind polymorphism in OOP.
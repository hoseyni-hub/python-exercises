# Library Management System

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"You borrowed {self.title}")
        else:
            print(f"{self.title} is not available.")

    def return_book(self):
        self.available = True
        print(f"You returned {self.title}")

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(book)


# Example usage:
book1 = Book("Python Basics", "John Doe")
book2 = Book("OOP Concepts", "Jane Smith")

library = Library()
library.add_book(book1)
library.add_book(book2)

library.display_books()
book1.borrow()
library.display_books()
book1.return_book()
library.display_books()

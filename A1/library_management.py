class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def display(self):
        print(self.title,"-",self.author)
        
class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title}  added successfully.")
    
    def show_book(self):
        for book in self.books:
            book.display()
    
    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"{title}   found.")
                return
        print(f"{title}  not found.")
        
    
    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.borrowed_books.append(book)
                print(f"{title}  borrowed successfully.")
                return
        print(f"{title} not found.")
                
    def return_book(self, title):
        for book in self.borrowed_books:
            if book.title.lower() == title.lower():
                self.borrowed_books.remove(book)
                print(f"{title}  returned successfully.")
                return
        print(f"{title} book not borrowed.")

library1 = Library()

# Adding books
library1.add_book(Book("Physics","Darpan"))
library1.add_book(Book("Mathematics","Alex"))

# Display books
library1.show_book()

# Search book
library1.search_book("Physics")
library1.search_book("Chemistry")

# Borrow book
library1.borrow_book("Mathematics")

# Return book
library1.return_book("Mathematics")
library1.return_book("Physics")
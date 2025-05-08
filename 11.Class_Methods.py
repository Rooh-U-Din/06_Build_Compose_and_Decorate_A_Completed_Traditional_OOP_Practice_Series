# 11. Class Methods

class Book:
    total_books = 0

    def __init__(self, books):
        self.books = books
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

Book.increment_book_count()
book1 = Book("book1")
print(Book.total_books)

Book.increment_book_count()
book2 = Book("book2")
print(Book.total_books)

Book.increment_book_count()
book3 = Book("book3")
print(Book.total_books)
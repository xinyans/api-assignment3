from enum import Enum


class Genre(Enum):
    UNDEFINED = 100
    SCIFI = 101
    FANTASY = 102
    HORROR = 103
    MYSTERY = 104


class Book:
    def __init__(self, isbn, title, author, genre, pub_year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.pub_year = pub_year


class BookDB:
    def __init__(self):
        self.db = {
            "ab12": Book("ab12", "The Hitchhiker's Guide to the Galaxy", "Douglas Adams", Genre.SCIFI, 1979),
            "cd34": Book("cd34", "A Game of Thrones", "George R. R. Martin", Genre.FANTASY, 1996),
            "ef56": Book("ef56", "Frankenstein", "Mary Shelley", Genre.HORROR, 1818),
            "gh78": Book("gh78", "My Notebook", "Xinyan Sun", Genre.UNDEFINED, 2022)
        }

    def get_book_by_isbn(self, isbn):
        return self.db.get(isbn, None)

    def add_book(self, book):
        if not book.isbn:
            return
        if book.isbn in self.db:
            return
        self.replace_book(book)

    def replace_book(self, book):
        if not book.isbn:
            return
        self.db[book.isbn] = book

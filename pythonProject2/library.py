import json
import os
from book import  Book

class Library:
    def __init__(self, filename="library.json"):  # Make filename parameter optional with a default value
        self.filename = filename
        self.books = []
        self.load_library()


    def add_book(self, title, author, publication_year, genre):
        new_book = Book(title, author, publication_year, genre)
        self.books.append(new_book)
        self.save_library()
   # def add_book(self, book):
    #    self.books.append(book)

    def list_books(self):
        if not self.books:
            print("Library is empty.")
        else:
            for index, book in enumerate(self.books, start=1):
                print(f"{index}. {book}")

    def edit_book(self, index, new_title, new_author, new_publication_year, new_genre):
        if 0 < index <= len(self.books):
            book = self.books[index - 1]
            book.title = new_title
            book.author = new_author
            book.publication_year = new_publication_year
            book.genre = new_genre
            print("Book details updated successfully.")
        else:
            print("Invalid book index.")

    def delete_book(self, index):
        if 0 < index <= len(self.books):
            del self.books[index - 1]
            print("Book deleted successfully.")
        else:
            print("Invalid book index.")
    def save_library(self, filename=None):
        if filename is None:
            filename = self.filename
        with open(filename, 'w') as file:
            json.dump([vars(book) for book in self.books], file)

    #def save_library(self, filename):
     #   with open(filename, 'w') as file:
      #      json.dump([vars(book) for book in self.books], file)

    def search_by_publication_year(self, publication_year):
        found_books = [book for book in self.books if book.publication_year == publication_year]
        if found_books:
            print(f"Books published in {publication_year}:")
            for book in found_books:
                print(book)
        else:
            print(f"No books found published in {publication_year}.")

    def load_library(self, filename=None):  # Make the filename parameter optional
        if filename is None:
            filename = self.filename
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                data = json.load(file)
                self.books = [Book(**book_data) for book_data in data]


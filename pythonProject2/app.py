import json
from library import Library
import os
from book import Book

def display_menu():
    print("\nPersonal Library Manager")
    print("1. Add Book")
    print("2. List Books")
    print("3. Edit Book")
    print("4. Delete Book")
    print("5. Search Books by Publication Year")
    print("6. Exit")

def main():

    library = Library("library.json")

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            publication_year = int(input("Enter publication year: "))
            genre = input("Enter genre: ")
            library.add_book(title, author, publication_year, genre)
            print("Book added successfully.")

        elif choice == '2':
            library.list_books()

        elif choice == '3':
            index = int(input("Enter index of book to edit: "))
            title = input("Enter new title: ")
            author = input("Enter new author: ")
            publication_year = int(input("Enter new publication year: "))
            genre = input("Enter new genre: ")
            library.edit_book(index - 1, title, author, publication_year, genre)

        elif choice == '4':
            index = int(input("Enter index of book to delete: "))
            library.delete_book(index - 1)

        elif choice == '5':
            publication_year = int(input("Enter publication year to search: "))
            library.search_by_publication_year(publication_year)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
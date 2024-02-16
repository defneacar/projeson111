# -*- coding: utf-8 -*-
"""son proje ödevi

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10mT-gSfFeBWxgTC2BDEwnNYSbT8sGvzH
"""

class Library:
    def __init__(self, file_name="books.txt"):
        self.file_name = file_name
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()

        if not books:
            print("No books found in the library.")
        else:
            for book in books:
                book_info = book.split(',')
                print(f"Book: {book_info[0]}, Author: {book_info[1]}")



    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")

        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print(f"Book '{title}' added successfully.")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")

        self.file.seek(0)
        books = self.file.read().splitlines()

        if any(title_to_remove in book for book in books):
            updated_books = [book for book in books if title_to_remove not in book]

            self.file.seek(0)
            self.file.truncate()
            self.file.writelines('\n'.join(updated_books))

            print(f"Book '{title_to_remove}' removed successfully.")
        else:
            print(f"Book '{title_to_remove}' not found in the library.")

lib = Library()

while True:
    print("*** MENU***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
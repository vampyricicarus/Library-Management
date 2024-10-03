class LibraryManagement:

    def __init__(self, book, user, author):
        self.__book = book
        self.__user = user
        self.__author = author

    def get_bookOperations(self):
        books = []
        while True:
            menu = input("Book Operations:\n1. Add a book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books\n6. Quit to main menu\n")
            if menu == "1":
                books.append(input("Which book to add? "))
            elif menu == "2":
                book_to_borrow = input("Which book to borrow? ")
                if book_to_borrow in books:
                    books.remove(book_to_borrow)
                else:
                    print("Book not found.")
            elif menu == "3":
                book_to_return = input("Return which book? ")
                if book_to_return not in books:
                    books.append(book_to_return)
                else:
                    print("Book already exists.")
            elif menu == "4":
                try:
                    index = books.index(input("What book are you looking for? "))
                    print(f"Book found at index: {index}")
                except ValueError:
                    print("Book not found.")
            elif menu == "5":
                print(books)
            elif menu == "6":
                break
            else:
                print("Invalid selection.")
        return self.__book
    
    def get_userOperations(self):
        users = []
        while True:
            menu = input("User Operations\n1. Add a new user\n2. View user details\n3. Display all users\n4. Quit to main menu\n")
            if menu == "1":
                users.append(input("Enter username: "))
            elif menu == "2":
                selectUser = input("Which username? ")
                print(selectUser)
            elif menu == "3":
                print(users)
            elif menu == "4":
                break
            else:
                print("Invalid selection.")
        return self.__user

    def get_authorOperations(self):
        authors = []
        while True:
            menu = input("Author Operations\n1. Add a new author\n2. View author details\n3. Display all authors\n4. Quit to main menu\n")
            if menu == "1":
                authors.append(input("Enter author name: "))
            elif menu == "2":
                author = input("Which author? ")
                print(author)
            elif menu == "3":
                print(authors)
            elif menu == "4":
                break
            else:
                print("Invalid selection.")
        return self.__author

library = LibraryManagement(None, None, None)
def main():
    while True:
        menu = input("Welcome to the Library Management System!\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit\n")
        if menu == "1":
            library.get_bookOperations()
        elif menu == "2":
            library.get_userOperations()
        elif menu == "3":
            library.get_authorOperations()
        elif menu == "4":
            break
        else:
            print("Invalid selection.")

main()
from book import Book

class Library:
    def __init__(self, books):
        self.books = books

    def show_books(self):
        print("The list of books is:")
        for index, book in enumerate(self.books):
            print(f"{index} - {book.name} - {book.tipo}")

    def loan_book(self):
        book_to_loan = int(input("Please enter the number of the book that you want: "))
        print(f"You have obtained this book: {self.books[book_to_loan].name}")
        self.books.pop(book_to_loan)

    def buy_book(self):
        book_to_buy = int(input("Please enter the number of the book that you want"))
        print(f"You have purchased this book: {self.books[book_to_buy].name}")
        self.books.pop(book_to_buy)

    def add_book(self):
        self.books.append(Book(input("Please enter the name:"),input("Please enter the category:")))

    def remove_book(self):
        book_to_remove = int(input("Please enter the number of the book that you want"))
        print(f"You have deleted this book: {self.books[book_to_remove].name}")
        self.books.pop(book_to_remove)
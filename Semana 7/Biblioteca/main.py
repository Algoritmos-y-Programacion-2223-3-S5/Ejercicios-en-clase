from book import Book
from library import Library


def add_books():
    return [
        Book("Harry Potter", "Ficcion"),
        Book("La materia oscura", "Ficcion"),
        Book("El señor de los anillos", "Ficcion"),
        Book("Don Quijote", "Aventura"),
        Book("El principito", "Infantil"),
        Book("Matematicas 5", "Educacion"),
        Book("Algebra de Baldor", "Educacion"),
        Book("La odisea", "Epica"),
        Book("La Iliada", "Epica"),
        Book("Sherlock", "Aventura")
    ]

def main():
    books = add_books()
    library = Library(books)
    print("**** Welcomeeeeeeeeeeeeeeeeeeeeeeee ****")
    while True:
        option = input("Please enter a option \n1- Show books\n2-Buy book\n3-Borrow book\n4-Add Book\n5-Remove Book\n-->")
        if option == "1":
            library.show_books()
        elif option == "2":
            library.buy_book()
        elif option == "3":
            library.loan_book()
        elif option == "4":
            library.add_book()
        elif option == "5":
            library.remove_book()
        elif option == "6":
            break
        else:
            print("Invalid option")

main()
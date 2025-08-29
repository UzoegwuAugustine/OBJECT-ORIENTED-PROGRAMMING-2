class Library:

    def __init__(self, list_of_books, name):
        self.bookslist = list_of_books
        self.name = name
        self.lendDict = {}
    
    def displayBooks(self):
        print(f"We have the following books in our library: {self.name}")
        for book in self.booklist:
            print(book)
    
    def lendBook(self, user, book):
        if book not in self.bookList:
            print("Sorry we do not have that book.")
        elif book in self.lendDict:
            print (f"The book is already being used by {self.lendDict[book]}")
        else:
            self.lendDict[book] = user
            print(
                "lender.Book database has been updated. You cn take the book now."
            )
    def addBook(self, book):
        self.booksList.append(book)
        print(f'{book} has been added to the book list ')

    def returnBook(self, book):
        if book in self.leendDict:
            del self.lendDict[book]
            print('book has been returned')
        else:
            print("That book wasn't borrowed from us.")

if __name__ == '__main__':
    books = Library(['Python', 'Rich Dad', 'Harry Potter'])
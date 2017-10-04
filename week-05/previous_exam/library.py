# https://github.com/greenfox-academy/retake-exam-basic-a/blob/master/library/library.py

class Book(object):

    def __init__(self, author, title, release_year):
        self.author = author
        self.title = title
        self.release_year = release_year


class BookShelf(object):

    def __init__(self):
        self.list_of_books = []

    
    def put(self, author, title, release_year):
        self.list_of_books.append(Book(author, title, release_year))


    def remove(self, title):
        books_removed = 0
        for book in self.list_of_books:
            if book.title == title:
                self.list_of_books.remove(book)
                books_removed += 1
        if books_removed == 0:
            return "This book is missing."


    def get_earliest_release(self):
        earliest_year = self.list_of_books[0].release_year
        for book in self.list_of_books:
            if book.release_year < earliest_year:
                earliest_year = book.release_year
                earliest_book = book
        return earliest_book


    def get_latest_release(self):
        latest_year = self.list_of_books[0].release_year
        for book in self.list_of_books:
            if book.release_year > latest_year:
                latest_year = book.release_year
                latest_book = book
        return latest_book


    def count_author_occurences(self):
        author_occurrences = {}
        for book in self.list_of_books:
            if book.author in author_occurrences.keys():
                author_occurrences[book.author] += 1
            else:
                author_occurrences[book.author] = 1
        return author_occurrences


    def get_favourite_author(self):
        author_occurrences = self.count_author_occurences()
        highest_occurence = max(list(author_occurrences.values()))
        favourite_author = list(author_occurrences.keys())[list(author_occurrences.values()).index(highest_occurence)]
        return favourite_author


    def books(self):
        if len(self.list_of_books) == 0:
            return "You have no books here."
        else:
            return  "You have {} books.".format(len(self.list_of_books)) + \
                    "\nEarliest release: {}: {} ({})".format(self.get_earliest_release().author, self.get_earliest_release().title, self.get_earliest_release().release_year) + \
                    "\nLatest release: {}: {} ({})".format(self.get_latest_release().author, self.get_latest_release().title, self.get_latest_release().release_year) + \
                    "\nFavourite author: " + self.get_favourite_author()

my_shelf = BookShelf()
print(my_shelf.books())

my_shelf.put("Douglas Adams", "The Hitchhiker's Guide to the Galaxy", 1979)
my_shelf.put("Douglas Adams", "Mostly Harmless", 1992)
my_shelf.put("Frank Herbert", "Dune", 1965)
my_shelf.put("Frank Herbert", "The Dragon in the Sea", 1957)
my_shelf.remove("The Dragon in the Sea")

print(my_shelf.books())


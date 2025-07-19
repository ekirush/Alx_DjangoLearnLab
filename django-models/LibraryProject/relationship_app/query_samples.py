from .models import Author, Book, Library, Librarian

from relationship_app.models import Author, Book, Library, Librarian


def books_by_author(author_id):
    author = Author.objects.get(id=author_id)
    return Book.objects.filter(author=author)


def books_in_library(library_id):
    library = Library.objects.get(id=library_id)
    return library.books.all()


def librarian_of_library(library_id):
    library = Library.objects.get(id=library_id)
    return Librarian.objects.get(library=library)

from .models import Author, Book, Library, Librarian

author = Author.objects.all()
books_by_author = Book.objects.filter(author=author)

books_library = Library.objects.all()

# Retrieve the librarian
library = Library.objects.all()


librarian = Librarian.objects.all()
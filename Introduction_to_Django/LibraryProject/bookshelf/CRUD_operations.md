## Create
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
<Book: 1984 by George Orwell (1949)>


## Retrieve
book.title, book.author, book.publication_year
('1984', 'George Orwell', 1949)


## Update
book.title = "Nineteen Eighty-Four"
book
<Book: Nineteen Eighty-Four by George Orwell (1949)>


## Delete
book.delete()
Book.objects.all()
# <QuerySet []>
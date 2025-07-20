from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Author, Book, Librarian, Library

# Create your views here.

def list_books(request):
    list_books = Book.objects.all()
    return render(request, "list_books.html", {"list_books": list_books})



class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

    



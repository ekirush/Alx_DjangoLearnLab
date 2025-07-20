from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.views.generic import View

from .models import Book, Library
from django.views.generic.detail import DetailView


# Function-based view for listing books
def list_books(request):
    list_books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"list_books": list_books})


# Class-based view for library detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# Registration view
class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
        return render(request, 'relationship_app/register.html', {'form': form})


# Logout view
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

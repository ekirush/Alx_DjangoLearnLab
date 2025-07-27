from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseForbidden
from .models import Book
from .forms import BookForm
from .forms import BookForm, ExampleForm


# -----------------------------
# View: List all books
# -----------------------------
@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    # Avoid exposing large datasets without pagination if this grows
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


# -----------------------------
# View: Create a new book
# -----------------------------
@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # ORM saves securely, preventing SQL injection
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})


# -----------------------------
# View: Edit a book
# -----------------------------
@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # get_object_or_404 prevents information leakage about object existence
    book = get_object_or_404(Book, id=book_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'bookshelf/book_form.html', {'form': form})


# -----------------------------
# View: Delete a book
# -----------------------------
@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    # Render a POST-only delete confirmation form with CSRF protection
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})

@login_required
def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Handle cleaned data safely
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            # For demo purposes: show confirmation
            return render(request, 'bookshelf/form_success.html', {'name': name})
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

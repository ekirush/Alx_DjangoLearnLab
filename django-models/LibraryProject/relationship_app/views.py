from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.detail import DetailView
from .models import Book, Library

from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"list_books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# This is the function-based view the check is expecting
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


def role_required(role_name):
    def check_role(user):
        return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == role_name
    return user_passes_test(check_role)



@role_required('Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@role_required('Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@role_required('Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')



from django.urls import path
from django.contrib.auth.views import LoginView
from .views import RegisterView, logout_view, list_books, LibraryDetailView

urlpatterns = [
    # Authentication
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

    # Book and Library Views
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

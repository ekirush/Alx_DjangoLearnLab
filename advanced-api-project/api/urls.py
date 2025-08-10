from django.urls import path
from .views import (
    BookListCreateView,  # Handles both list and create
    BookRetrieveUpdateDestroyView  # Handles retrieve, update, delete
)

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
]

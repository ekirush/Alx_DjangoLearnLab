from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/create/', views.create_book, name='create_book'),
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
    
    # 👇 New route for ExampleForm
    path('example-form/', views.example_form_view, name='example_form'),
]

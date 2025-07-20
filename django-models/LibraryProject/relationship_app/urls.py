from django.urls import path
from . import views
from .views import list_books
from .views import LoginView, logout_view, RegisterView

urlpatterns = [
    path('books/', views.list_books, name='list_books' ),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name = "library_detail"),
     path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
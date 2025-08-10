from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# --- ListView ---
class BookListView(generics.ListAPIView):
    """
    GET: List all books with filtering, searching, and ordering.
    Filtering: ?title=SomeTitle&author=1&publication_year=2020
    Search: ?search=harry
    Ordering: ?ordering=title  or  ?ordering=-publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering by field names
    filterset_fields = ['title', 'author', 'publication_year']

    # Search by title and author's name (double underscore for related field)
    search_fields = ['title', 'author__name']

    # Allow ordering by title or publication_year
    ordering_fields = ['title', 'publication_year']

    # Default ordering if none is specified
    ordering = ['title']


# --- DetailView ---
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves details of a single book by ID.
    Public access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# --- CreateView ---
class BookCreateView(generics.CreateAPIView):
    """
    Creates a new book entry.
    Authenticated access only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


# --- UpdateView ---
class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing book entry.
    Authenticated access only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


# --- DeleteView ---
class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes a book entry.
    Authenticated access only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
from rest_framework import filters


# --- ListView ---
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [
        rest_framework.DjangoFilterBackend,  # uses the imported alias
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
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

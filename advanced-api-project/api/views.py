from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# --- ListView ---
class BookListView(generics.ListAPIView):
    """
    Retrieves a list of all books.
    Public access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# --- DetailView ---
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves details of a single book by ID.
    Public access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# --- CreateView ---
class BookCreateView(generics.CreateAPIView):
    """
    Creates a new book entry.
    Authenticated access only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

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
    permission_classes = [permissions.IsAuthenticated]

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

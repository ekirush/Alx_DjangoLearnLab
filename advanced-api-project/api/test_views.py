from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(TestCase):
    """
    Unit tests for Book API endpoints:
    - CRUD operations
    - Filtering, searching, ordering
    - Permissions and authentication
    """

    def setUp(self):
        # Create test users
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.other_user = User.objects.create_user(username="otheruser", password="otherpass")

        # Create an author
        self.author = Author.objects.create(name="Author One")

        # Create books
        self.book1 = Book.objects.create(title="Book One", publication_year=2000, author=self.author)
        self.book2 = Book.objects.create(title="Another Book", publication_year=2010, author=self.author)

        # API client
        self.client = APIClient()

        # Endpoints
        self.list_url = "/api/books/"
        self.detail_url = f"/api/books/{self.book1.pk}/"
        self.create_url = "/api/books/create/"
        self.update_url = f"/api/books/{self.book1.pk}/update/"
        self.delete_url = f"/api/books/{self.book1.pk}/delete/"

    def test_list_books_public(self):
        """Anyone can list books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book_public(self):
        """Anyone can retrieve a book"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    def test_create_book_authenticated(self):
        """Authenticated users can create books"""
        self.client.login(username="testuser", password="testpass")
        data = {
            "title": "New Book",
            "publication_year": 2022,
            "author": self.author.pk
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Unauthenticated users cannot create books"""
        data = {"title": "No Auth", "publication_year": 2020, "author": self.author.pk}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        """Authenticated users can update books"""
        self.client.login(username="testuser", password="testpass")
        data = {"title": "Updated Title", "publication_year": 2005, "author": self.author.pk}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_update_book_unauthenticated(self):
        """Unauthenticated users cannot update books"""
        data = {"title": "No Change", "publication_year": 2001, "author": self.author.pk}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_authenticated(self):
        """Authenticated users can delete books"""
        self.client.login(username="testuser", password="testpass")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_delete_book_unauthenticated(self):
        """Unauthenticated users cannot delete books"""
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_filter_books_by_title(self):
        """Filter books by title"""
        response = self.client.get(f"{self.list_url}?title=Book One")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Book One")

    def test_search_books_by_title(self):
        """Search books by keyword"""
        response = self.client.get(f"{self.list_url}?search=Another")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Another Book")

    def test_order_books_by_publication_year(self):
        """Order books by publication year descending"""
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))

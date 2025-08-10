# API Endpoints

## Books
- GET /api/books/ — List all books (public)
- GET /api/books/<id>/ — Retrieve single book (public)
- POST /api/books/create/ — Create a book (authenticated only)
- PUT /api/books/<id>/update/ — Update a book (authenticated only)
- DELETE /api/books/<id>/delete/ — Delete a book (authenticated only)

## Permissions
- Read: Public
- Write: Authenticated users only

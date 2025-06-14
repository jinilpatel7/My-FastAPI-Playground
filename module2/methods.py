"""
Create RESTful endpoints using HTTP methods (GET, POST, PUT, DELETE)

Use path parameters to capture dynamic values in URLs

Use query parameters to filter or modify behavior

Handle optional and typed parameters

HTTPException
"""

"""
What are RESTful Endpoints?
REST (Representational State Transfer) is a set of rules for building web APIs. FastAPI makes it easy to follow REST principles by using HTTP methods like:

Method	    Used for    	Example URL
GET	        Read data	    /books/1
POST	    Create data	    /books
PUT	        Update data	    /books/1
DELETE	    Delete data	    /books/1
"""

# now put all four REST methods (GET, POST, PUT, DELETE) into practice using FastAPI with a hands-on Book Management API.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    description: Optional[str] = None

books: List[Book] = [
    Book(id=1, title="1984", author="George Orwell", description="Dystopian novel."),
    Book(id=2, title="Sapiens", author="Yuval Noah Harari"),
    Book(id=3, title="To Kill a Mockingbird", author="Harper Lee", description="Classic novel about racial injustice."),
    Book(id=4, title="The Great Gatsby", author="F. Scott Fitzgerald", description="A novel set in the Roaring Twenties."),
    Book(id=5, title="Brave New World", author="Aldous Huxley", description="A futuristic society controlled by technology."),
    Book(id=6, title="Atomic Habits", author="James Clear", description="Self-help book on habit building."),
    Book(id=7, title="The Catcher in the Rye", author="J.D. Salinger", description="Coming-of-age story."),
    Book(id=8, title="The Alchemist", author="Paulo Coelho", description="A journey of self-discovery."),
    Book(id=9, title="Thinking, Fast and Slow", author="Daniel Kahneman", description="Insights into human thinking and decision making."),
    Book(id=10, title="Deep Work", author="Cal Newport", description="Rules for focused success in a distracted world.")
]

# Get all books API

@app.get("/books")
def get_all_books():
    return books

# Get book by id
@app.get("/book/{book_id}")
def get_book(book_id: int):
    for b in books:
        if b.id == book_id:
            return b
    raise HTTPException(status_code=404, detail="Book Not Found")

# POST: Add a new book
@app.post("/addbooks")
def add_book(addbook: Book):
    for existing in books:
        if existing.id == addbook.id:
            raise HTTPException(status_code=400, detail="Book with the same id already exist")
    
    books.append(addbook)
    return addbook

# PUT: Update a book
@app.put("/book/{book_id}")
def update_book(book_id: int, updated_book:Book):
    for i, book in enumerate(books):
        if book.id == book_id:
            books[i] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

# DELETE: Remove a book
@app.delete("/delbooks/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(books):
        if book.id == book_id:
            del books[i]
            return {"message": f"Book with ID {book_id} deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
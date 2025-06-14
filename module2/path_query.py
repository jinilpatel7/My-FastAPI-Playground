# here i will learn  Path Parameters (Dynamic URLs),  Query Parameters (Optional Filters), and Combine Path + Query Parameters 
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

@app.get("/books")
def get_all_books():
    return books

"""
1. Path Parameters (Dynamic URLs)
Theory
Path parameters are variables in the URL path. They are required and used to identify a specific resource.

Example URL:
    /books/3
    Here, 3 is the book_id.
"""

# a) Get book by ID
@app.get("/book/{book_id}")
def get_book(book_id: int):
    for i in books:
        if i.id == book_id:
            return i
    raise HTTPException(status_code=404, detail="Book not found")

# b) Delete book by ID
@app.delete("/book/{book_id}")
def del_book(book_id: int):
    for i, book in enumerate(books):
        if book.id == book_id:
            del books[i]
            return {"message": f"Book with ID {book_id} deleted"}
    raise HTTPException(status_code=404, detail="Book not found")

"""
2. Query Parameters (Optional Filters)
Theory
Query parameters are optional and used to filter or modify results.
Example URL:
    /books/search?author=Orwell
"""
# Search books by author
@app.get("/books/search")
def sba(author: Optional[str] = None):
    if author:
        results = [b for b in books if b.author.lower() == author.lower()]
        if not results:
            raise HTTPException(status_code=404, detail=f"No books found by author '{author}'")
        return results
    return books # return all if no author filter

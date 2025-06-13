# Mini‑Project 1: “Quote of the Day” API
"""
Requirements
Endpoint: GET /quote

Returns a random quote from a list of at least 5 quotes you hard‑code.

Bonus: Add GET /quotes to return the full list.
"""
import random
from fastapi import FastAPI

QUOTES = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Life is what happens when you're busy making other plans. – John Lennon",
    "A room without books is like a body without a soul. - Marcus Tullius Cicero",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "If you tell the truth, you don't have to remember anything. - Mark Twain"
]

app = FastAPI()

# Route to get random quote from list
@app.get("/quote")
def qotd():
    return {"Quote Of The Day": random.choice(QUOTES)}

# Route to get all qoutes

@app.get("/allquote")
def allq():
    return {"quotes": QUOTES}
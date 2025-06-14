#  Product Catalog API — from scratch — including everything you asked for:

"""
CRUD operations
Path parameters
Query parameters
Combined path + query parameters
In-memory data store
"""
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    category: str
    price: float
    in_stock: bool = True
    description: Optional[str] = None

products: List[Product] = [
    # Electronics
    Product(id=1, name="Smartphone X200", category="Electronics", price=699.99, description="A powerful smartphone with an amazing camera."),
    Product(id=2, name="Bluetooth Speaker", category="Electronics", price=49.99, description="Portable and waterproof speaker with deep bass."),
    Product(id=3, name="Wireless Headphones", category="Electronics", price=89.99, description="Noise-cancelling over-ear headphones."),

    # Fashion
    Product(id=4, name="Running Shoes", category="Fashion", price=59.99, description="Lightweight shoes for daily workouts."),
    Product(id=5, name="Leather Wallet", category="Fashion", price=29.99, description="Genuine leather wallet with card slots."),
    Product(id=6, name="Denim Jacket", category="Fashion", price=79.99, description="Trendy and durable denim jacket."),

    # Home & Kitchen
    Product(id=7, name="Non-stick Frying Pan", category="Home & Kitchen", price=24.99, description="Scratch-resistant and easy to clean."),
    Product(id=8, name="Electric Kettle", category="Home & Kitchen", price=34.99, description="Boils water quickly and safely."),
    Product(id=9, name="Vacuum Cleaner", category="Home & Kitchen", price=129.99, description="High-power suction with HEPA filter."),

    # Books
    Product(id=10, name="The Psychology of Money", category="Books", price=14.99, description="Timeless lessons on wealth and behavior."),
    Product(id=11, name="Deep Work", category="Books", price=13.99, description="Strategies for focused success."),
    Product(id=12, name="Atomic Habits", category="Books", price=16.99, description="Build good habits and break bad ones."),
]

# Get all products (With optional query params)
@app.get("/products")
def get_all_products(
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    in_stock: Optional[bool] = None,
):
    results = products

    if category:
        results = [ p for p in results if p.category.lower() == category.lower()]
    if min_price is not None:
        results = [p for p in results if p.price >= min_price]
    if max_price is not None:
        results = [p for p in results if p.price <= min_price]
    if in_stock is not None:
        results = [p for p in results if p.in_stock == in_stock]
    return results

# GET Single Product by ID (path param)

@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

# POST: Add New Product

@app.post("/products")
def add_prod(new_product: Product):
    for p in products:
        if p.id == new_product.id:
            raise HTTPException(status_code=400, detail="Product ID already exist")
    products.append(new_product)
    return new_product

# PUT: Update Product
@app.put("/products/{product_id}")
def update_prod(product_id: int, updated: Product):
    for i, product in enumerate(products):
        if product.id == product_id:
            products[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Product Not Found")

# DELETE Product
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for i, product in enumerate(products):
        if product.id == product_id:
            del products[i]
            return {"message": f"Product {product_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Product not found")

# Combine Path + Query Example
# Get a user's cart, but optionally filter by in-stock status.
@app.get("/users/{user_id}/cart")
def get_user_cart(user_id: int, in_stock: Optional[bool] = None):
    # Simulate: All users have same cart for this demo
    cart = [p for p in products if p.id in [1, 3]]

    if in_stock is not None:
        cart = [p for p in cart if p.in_stock == in_stock]

    return {
        "user_id": user_id,
        "cart": cart
    }

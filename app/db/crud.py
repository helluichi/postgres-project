from sqlalchemy.orm import Session
from app.db import models

# CRUD для Category
def create_category(db: Session, title: str):
    category = models.Category(title=title)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def get_all_categories(db: Session):
    return db.query(models.Category).all()

def get_books_by_category(db: Session, category_id: int):
    return db.query(models.Book).filter(models.Book.category_id == category_id).all()

# CRUD для Book
def create_book(db: Session, title: str, description: str, price: float, category_id: int, url: str = ''):
    book = models.Book(
        title=title,
        description=description,
        price=price,
        url=url,
        category_id=category_id
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def get_all_books(db: Session):
    return db.query(models.Book).all()

def update_book_price(db: Session, book_id: int, new_price: float):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book:
        book.price = new_price
        db.commit()
        db.refresh(book)
    return book

def delete_book(db: Session, book_id: int):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
    return book

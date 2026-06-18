from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.db import Base

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, nullable=False)  # Название категории
    description = Column(String, nullable=True)          # Описание категории
    
    books = relationship("Book", back_populates="category")

class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)          # Название книги
    description = Column(String, nullable=True)     # Описание книги
    price = Column(Float, nullable=False)           # Цена книги
    url = Column(String, nullable=True)             # Ссылка на товар
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    
    category = relationship("Category", back_populates="books")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import books, categories

app = FastAPI(
    title="Bookstore API",
    description="API для управления книгами и категориями",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем роутеры
app.include_router(books.router)
app.include_router(categories.router)

@app.get("/")
def root():
    return {"message": "Welcome to Bookstore API", "docs": "/docs", "redoc": "/redoc"}

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API is running"}

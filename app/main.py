from app.db.db import SessionLocal
from app.db import crud

db = SessionLocal()

print("\n" + "="*60)
print("СОДЕРЖИМОЕ БАЗЫ ДАННЫХ")
print("="*60 + "\n")

categories = crud.get_all_categories(db)

for cat in categories:
    print(f"📚 Категория: {cat.title}")
    print("-"*40)
    
    books = crud.get_books_by_category(db, cat.id)
    for book in books:
        print(f"  📖 {book.title}")
        print(f"     Описание: {book.description}")
        print(f"     Цена: {book.price} руб.")
        print(f"     Ссылка: {book.url or 'пока пустая'}")
        print()
    
print("="*60 + "\n")

db.close()

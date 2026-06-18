import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.db.db import SessionLocal, engine, Base
from app.db import crud

def init_db():
    # Создаём таблицы
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    try:
        # Создаём категории
        categories = [
            ("Фантастика", "Научная фантастика и фэнтези"),
            ("Детектив", "Криминальные романы и детективы"),
            ("Классика", "Мировая классическая литература"),
        ]
        
        for title, desc in categories:
            if not crud.get_category_by_title(db, title):
                crud.create_category(db, title, desc)
                print(f"✓ Создана категория: {title}")
        
        # Создаём книги (поля: title, description, price, url, category_title)
        books_data = [
            ("1984", "Роман-антиутопия", 15.99, "https://example.com/1984", "Фантастика"),
            ("Дюна", "Научно-фантастический роман", 19.99, "https://example.com/dune", "Фантастика"),
            ("Убийство в Восточном экспрессе", "Классический детектив", 12.50, "https://example.com/express", "Детектив"),
            ("Преступление и наказание", "Психологический роман", 14.99, "https://example.com/crime", "Классика"),
        ]
        
        for title, desc, price, url, cat_title in books_data:
            crud.create_book(
                db, 
                title=title, 
                description=desc, 
                price=price, 
                url=url, 
                category_title=cat_title
            )
            print(f"  ✓ Добавлена книга: {title}")
        
        db.commit()
        print("\n✅ База данных инициализирована успешно!")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_db()

from app.db.db import SessionLocal
from app.db.db import Base, engine
from app.db import crud

# Создаём таблицы
Base.metadata.create_all(bind=engine)

db = SessionLocal()

try:
    # Добавляем 2 категории
    cat1 = crud.create_category(db, "Фантастика")
    cat2 = crud.create_category(db, "Программирование")
    
    # Добавляем книги (2-4 на категорию)
    crud.create_book(db, "Дюна", "Эпичная научная фантастика", 599, cat1.id)
    crud.create_book(db, "1984", "Классическая антиутопия", 450, cat1.id)
    crud.create_book(db, "Солярис", "Философская фантастика", 499, cat1.id)
    
    crud.create_book(db, "Clean Code", "Идеальный код", 1200, cat2.id)
    crud.create_book(db, "Python для всех", "Основы Python", 800, cat2.id)
    crud.create_book(db, "Алгоритмы", "Алгоритмы и структуры данных", 1500, cat2.id)
    
    print("✅ База данных инициализирована успешно!")
    
except Exception as e:
    print(f"❌ Ошибка: {e}")
    db.rollback()
finally:
    db.close()

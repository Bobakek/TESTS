import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Определяем абсолютный путь к базе данных
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL = f'sqlite:///{os.path.join(BASE_DIR, "../taskmanager.db")}'

# Создаем движок для базы данных
engine = create_engine(DATABASE_URL, echo=True)

# Создаем локальную сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
class Base(DeclarativeBase):
    pass

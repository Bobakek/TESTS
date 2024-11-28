from app.models.user import User
from app.models.task import Task


from app.backend.db import Base, engine


# Генерация таблиц
Base.metadata.create_all(bind=engine)

# Печать SQL-запросов для создания таблиц
print(str(User.__table__))
print(str(Task.__table__))


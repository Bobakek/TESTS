from pydantic import BaseModel

# Модель для создания пользователя
class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int

# Модель для обновления пользователя
class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int

# Модель для создания задачи
class CreateTask(BaseModel):
    title: str
    content: str
    priority: int = 0
    completed: bool = False

# Модель для обновления задачи
class UpdateTask(BaseModel):
    title: str
    content: str
    priority: int
    completed: bool

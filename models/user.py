from sqlalchemy import Column, Integer, String, insert, select, update, delete
from sqlalchemy.orm import relationship, Session
from fastapi import HTTPException, APIRouter, Depends, status
from typing import Annotated
from app.models.shared import User
from slugify import slugify
from app.backend.db import Base
from app.backend.db_depends import get_db
from app.routers.schemas import CreateUser, UpdateUser


router = APIRouter()

# class User(Base):
#     __tablename__ = 'users'
#
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, nullable=False)
#     firstname = Column(String, nullable=False)
#     lastname = Column(String, nullable=False)
#     age = Column(Integer, nullable=True)
#     slug = Column(String, unique=True, index=True)
#
#     # Связь с таблицей Task через строковую ссылку
#     tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan")

# Функция для получения всех пользователей
@router.get("/")
async def all_users(db: Annotated[Session, Depends(get_db)]):
    from app.models.user import User
    users = db.scalars(select(User)).all()
    return users

# Функция для получения пользователя по ID
@router.get("/{user_id}")
async def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    from app.models.user import User
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    return user

# Функция для получения всех задач пользователя
@router.get("/{user_id}/tasks")
async def tasks_by_user_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    from app.models.user import User
    from app.models.task import Task

    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    tasks = db.scalars(select(Task).where(Task.user_id == user_id)).all()
    return tasks

# Функция для удаления пользователя
@router.delete("/delete/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    from app.models.user import User
    from app.models.task import Task

    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    db.delete(user)  # Связанные задачи будут удалены каскадно
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "User and all related tasks deleted successfully!"}
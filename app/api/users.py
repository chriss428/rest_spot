from fastapi import APIRouter
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.database.db_cnt import async_session_maker
from app.database.models.models_tables import User

router = APIRouter(prefix="/users", tags=["Пользователи"])

@router.get("/", summary="Получить всеx пользователей")
async def get_all_users():
    async with async_session_maker() as session:
        query = select(User)
        result = await session.execute(query)
        users = result.scalars().all()
        return users

@router.get("/{id}", summary="Получить пользователя по id")
async def get_one_user(user_id: int):
    async with async_session_maker() as session:
        query = select(User).options(selectinload(User.place)).where(User.id == user_id)
        result = await session.execute(query)
        users = result.scalar_one_or_none()
        return users


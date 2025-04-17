from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.database.db_cnt import async_session_maker
from app.users.model import User


async def get_user(user_id: int):
    async with async_session_maker() as session:
        query = select(User).options(selectinload(User.wish_places)).where(User.id == user_id)
        result = await session.execute(query)
        user = result.scalar_one_or_none()
        return user


async def get_auth_user_or_none_by_id(user_id: int):
    async with async_session_maker() as session:
        query = select(User).options(selectinload(User.wish_places)).where(User.id == user_id)
        result = await session.execute(query)
        users = result.scalar_one_or_none()
        return users


async def create_user(user_data: dict):
    async with async_session_maker() as session:
        async with session.begin():
            new_user = User(**user_data)
            session.add(new_user)
            session.commit()
            return new_user


async def get_auth_user_or_none(email: str):
    async with async_session_maker() as session:
        query = select(User).where(User.email == email)
        result = await session.execute(query)
        users = result.scalar_one_or_none()
        return users

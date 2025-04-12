from sqlalchemy import select
from app.database.db_cnt import async_session_maker
from app.database.models.models_tables import User


async def get_auth_user_or_none(email: str):
    async with async_session_maker() as session:
        query = select(User).where(User.email == email)
        result = await session.execute(query)
        users = result.scalar_one_or_none()
        return users

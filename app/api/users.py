from fastapi import APIRouter
from sqlalchemy import select
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

# @router.post("/create/", summary="Добавить нового пользователя")
# async def create_user(user: )
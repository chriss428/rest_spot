from fastapi import APIRouter
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.database.db_cnt import async_session_maker
from app.users.model import User, UserPlaceAssoc
from app.users.schema import SWishAddResponse

router = APIRouter(prefix="/users", tags=["Пользователи"])

# @router.get("/", summary="Получить всеx пользователей")
# async def get_all_users():
#     async with async_session_maker() as session:
#         query = select(User)
#         result = await session.execute(query)
#         users = result.scalars().all()
#         return users

@router.get("/{id}", summary="Получить пользователя по id")
async def get_user_by_id(user_id: int):
    async with async_session_maker() as session:
        query = select(User).options(selectinload(User.wish_places)).where(User.id == user_id)
        result = await session.execute(query)
        users = result.scalar_one_or_none()
        return users

@router.post("/add_wish_place/", summary="Добавление в избранное", response_model=SWishAddResponse)
async def add_wish_place(user_id: int, place_id: int):
    async with async_session_maker() as session:
        existing = await session.scalar(
            select(UserPlaceAssoc)
            .where(UserPlaceAssoc.user_id == user_id)
            .where(UserPlaceAssoc.place_id == place_id)
        )

        if not existing:
            new_wish_place = UserPlaceAssoc(user_id=user_id, place_id=place_id)
            session.add(new_wish_place)
            await session.commit()
            return {"success": True, "message": "Added to wishlist", "data": new_wish_place}
        else:
            return {"success": False, "message": "Already in wishlist", "data": None}


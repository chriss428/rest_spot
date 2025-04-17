from fastapi import HTTPException
from sqlalchemy import select, update
from fastapi.params import Depends
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import SQLAlchemyError
from app.database.db_cnt import async_session_maker
from app.users.model import User, UserPlaceAssoc
from app.authentication.dependencies import get_current_admin_user


async def get_all_users_with_places():
    async with async_session_maker() as session:
        query = select(User).options(selectinload(User.wish_places))
        result = await session.execute(query)
        users = result.scalars().all()
        return users


async def user_by_id(user_id: int):
    async with async_session_maker() as session:
        query = select(User).options(selectinload(User.wish_places)).where(User.id == user_id)
        result = await session.execute(query)
        users = result.scalar_one_or_none()
        return users


async def wish_place(place_id: int, user_data: User):
    async with async_session_maker() as session:
        existing = await session.scalar(
            select(UserPlaceAssoc)
            .where(UserPlaceAssoc.user_id == user_data.id)
            .where(UserPlaceAssoc.place_id == place_id)
        )

        if not existing:
            new_wish_place = UserPlaceAssoc(user_id=user_data.id, place_id=place_id)
            session.add(new_wish_place)
            await session.commit()
            return {"success": True, "message": "Added to wishlist", "data": new_wish_place}
        else:
            return {"success": False, "message": "Already in wishlist", "data": None}


async def assigning_admin(user_id: int, admin = Depends(get_current_admin_user)):
    async with async_session_maker() as session:
        async with session.begin():
            stmt = select(User).where(User.id == user_id)
            user = (await session.execute(stmt)).scalar_one_or_none()
            if not user:
                raise HTTPException(status_code=404, detail="Пользователь не найден")

            query = (update(User)
                     .where(User.id == user_id)
                     .values(is_admin=True)
                     .execution_options(synchronize_session="fetch")
            )
            await session.execute(query)
            updated_user = (await session.execute(select(User).where(User.id == user_id))).scalar_one()
            try:
                await session.commit()
            except SQLAlchemyError as e:
                await session.rollback()
                raise e
            return updated_user

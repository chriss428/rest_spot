from certifi import where
from fastapi import APIRouter
from sqlalchemy import select
from app.database.db_cnt import async_session_maker
from app.database.models.models_tables import User_Place
from app.database.models.schemas import SWishAddResponse


router = APIRouter(prefix="/wishes", tags=["Избранные места отдыха"])

@router.post("/add/", summary="Добавление в избранное", response_model=SWishAddResponse)
async def add_wish_place(user_id: int, place_id: int):
    async with async_session_maker() as session:
        existing = await session.scalar(
            select(User_Place)
            .where(User_Place.user_id == user_id)
            .where(User_Place.place_id == place_id)
        )

        if not existing:
            new_wish_place = User_Place(user_id=user_id, place_id=place_id)
            session.add(new_wish_place)
            await session.commit()
            return {"success": True, "message": "Added to wishlist", "data": new_wish_place}
        else:
            return {"success": False, "message": "Already in wishlist", "data": None}


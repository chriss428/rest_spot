from fastapi import APIRouter
from sqlalchemy import select
from app.database.db_cnt import async_session_maker
from app.database.models.models_tables import Place

router = APIRouter(prefix="/places", tags=["Места отдыха"])

@router.get("/", summary="Получить все места отдыха")
async def get_all_places():
    async with async_session_maker() as session:
        query = select(Place)
        result = await session.execute(query)
        places = result.scalars().all()
        return places

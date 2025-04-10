from fastapi import APIRouter
from sqlalchemy import select
from app.database.db_cnt import async_session_maker
from app.database.models.models_tables import Place
from app.database.models.schemas import SPlaceAdd

router = APIRouter(prefix="/places", tags=["Места отдыха"])

@router.get("/", summary="Получить все места отдыха")
async def get_all_places():
    async with async_session_maker() as session:
        query = select(Place)
        result = await session.execute(query)
        places = result.scalars().all()
        return places

@router.post("/add/", summary="Добавить место отдыха", response_model=SPlaceAdd)
async def add_place(place: SPlaceAdd):
    async with async_session_maker() as session:
        async with session.begin():
            new_place = Place(**place.model_dump())
            session.add(new_place)
            await session.commit()
            return new_place
from sqlalchemy import select
from app.database.db_cnt import async_session_maker
from app.places.model import Place
from app.places.schema import SPlaceAdd


async def get_all_places():
    async with async_session_maker() as session:
        query = select(Place)
        result = await session.execute(query)
        places = result.scalars().all()
        return places


async def add_place(place: SPlaceAdd):
    async with async_session_maker() as session:
        async with session.begin():
            new_place = Place(**place.model_dump())
            session.add(new_place)
            await session.commit()
            return new_place
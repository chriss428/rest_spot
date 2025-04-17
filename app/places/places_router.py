from fastapi import APIRouter, Depends
from app.places.schema import SPlaceAdd
from app.authentication.dependencies import get_current_admin_user
from app.places.crud import get_all_places, add_place


router = APIRouter(prefix="/places", tags=["Места отдыха"])


@router.get("/", summary="Получить все места отдыха")
async def get_places():
    return await get_all_places()


@router.post("/add/", summary="Добавить место отдыха", response_model=SPlaceAdd)
async def add_place_by_admin(place: SPlaceAdd, admin = Depends(get_current_admin_user)):
    return await add_place(place)
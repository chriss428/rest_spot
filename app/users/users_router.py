from fastapi import APIRouter, Depends
from app.users.model import User
from app.users.schema import SWishAddResponse
from app.authentication.dependencies import get_current_user
from app.users.crud import wish_place

router = APIRouter(prefix="/users", tags=["Пользователи"])


@router.post("/add_wish_place/", summary="Добавление в избранное", response_model=SWishAddResponse)
async def add_wish_place(place_id: int, user_data: User = Depends(get_current_user)):
    return await wish_place(place_id, user_data)


@router.get("/me/", summary="Получить данные о текущем пользователе")
async def get_me(user_data: User = Depends(get_current_user)):
    return user_data
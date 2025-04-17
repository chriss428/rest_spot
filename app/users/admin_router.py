from fastapi import APIRouter, Depends
from app.users.model import User
from app.authentication.dependencies import get_current_admin_user
from app.users.crud import get_all_users_with_places, user_by_id, assigning_admin


router = APIRouter(prefix="/admin_fanc", tags=["Функции администратора"])

@router.get("/all_users/", summary="Просмотр всех пользователей")
async def get_users_with_places(user_data: User = Depends(get_current_admin_user)):
    return await get_all_users_with_places()


@router.get("/{id}", summary="Получить пользователя по id")
async def get_user_by_id(user_id: int, user_data: User = Depends(get_current_admin_user)):
    return await user_by_id(user_id)


@router.put("/assigning_admin/", summary="Назначение роли администратора пользователю")
async def add_admin(user_id: int, admin: User = Depends(get_current_admin_user)):
    return await assigning_admin(user_id)

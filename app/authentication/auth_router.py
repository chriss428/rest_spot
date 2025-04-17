from fastapi import APIRouter, Response
from app.exceptions import UserAlreadyExistsException, IncorrectEmailOrPasswordException
from app.authentication.auth import get_password_hash, authenticate_user, create_access_token
from app.authentication.cshema import SUserRegister, SUserAuth
from app.authentication.crud import create_user, get_auth_user_or_none

router = APIRouter(prefix="/auth", tags=["Регистрация/Аутентификация"])


@router.post("/register/", summary="Регистрация пользователя")
async def register_user(user_data: SUserRegister):
    user = await get_auth_user_or_none(email=user_data.email)
    if user:
        raise UserAlreadyExistsException
    user_dict = user_data.model_dump()
    user_dict['password'] = get_password_hash(user_data.password)
    await create_user(user_dict)
    return {'message': f'Вы успешно зарегистрированы!'}


@router.post("/login/", summary="Аутентификация пользователя")
async def auth_user(response: Response, user_data: SUserAuth):
    check = await authenticate_user(email=user_data.email, password=user_data.password)
    if check is None:
        raise IncorrectEmailOrPasswordException
    access_token = create_access_token({"sub": str(check.id)})
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)
    return {'ok': True, 'access_token': access_token, 'refresh_token': None, 'message': 'Авторизация успешна!'}


@router.post("/logout/", summary="Выход из системы")
async def logout_user(response: Response):
    response.delete_cookie(key="users_access_token")
    return {'message': 'Пользователь успешно вышел из системы'}
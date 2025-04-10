from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


class SPlaceAdd(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int|None
    name: str = Field(min_length=1, max_length=50, description="Название места отдыха, длина от 1 до 50 символов")
    latitude: float = Field(ge=-90, le=90, description="Широта, число с плавающей точкой")
    longitude: float = Field(ge=-180, le=180, description="Долгота, число с плавающей точкой")

class SUserCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int|None
    email: str = Field(min_length=1, max_length=50, description="Адрес электронной почты")
    password: str

class SWishAdd(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id : int
    place_id: int

class SWishAddResponse(BaseModel):
    success: bool
    message: str
    data: Optional[SWishAdd] = None
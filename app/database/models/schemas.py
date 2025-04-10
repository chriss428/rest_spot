from pydantic import BaseModel, ConfigDict, Field, field_validator
from datetime import date, datetime


class SPlaceAdd(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int|None = None
    name: str = Field(min_length=1, max_length=50, description="Название места отдыха, длина от 1 до 50 символов")
    latitude: float = Field(ge=-90, le=90, description="Широта, число с плавающей точкой")
    longitude: float = Field(ge=-180, le=180, description="Долгота, число с плавающей точкой")

# class SUser(BaseModel):
#     id: int
#
# class SUserCreate(BaseModel):
#     model_config = ConfigDict(from_attributes=True)
#
#     full_name: str = Field(min_length=1, max_length=50, description="ФИО пользователя, длина от 1 до 50 символов")
#     date_of_birth: date = Field(description="Дата рождения в формате ГГГГ-ММ-ДД")
#     email: str = mapped_column(String(50), unique=True)
#     password: Mapped[str] = mapped_column(String(150), unique=True)
#
#     @field_validator("date_of_birth")
#     @classmethod
#     def validate_date_of_birth(cls, values: date):
#         if values and values >= datetime.now().date():
#             raise ValueError('Дата рождения должна быть в прошлом')
#         return values
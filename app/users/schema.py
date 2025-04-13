from pydantic import BaseModel, ConfigDict
from typing import Optional


# class SUserCreate(BaseModel):
#     model_config = ConfigDict(from_attributes=True)
#
#     id: int|None
#     email: str = Field(min_length=1, max_length=50, description="Адрес электронной почты")
#     password: str

class SWishAdd(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id : int
    place_id: int

class SWishAddResponse(BaseModel):
    success: bool
    message: str
    data: Optional[SWishAdd] = None
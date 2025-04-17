from pydantic import BaseModel, ConfigDict
from typing import Optional


class SWishAdd(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id : int
    place_id: int

class SWishAddResponse(BaseModel):
    success: bool
    message: str
    data: Optional[SWishAdd] = None
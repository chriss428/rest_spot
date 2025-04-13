from pydantic import BaseModel, ConfigDict, Field


class SPlaceAdd(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int|None = None
    name: str = Field(..., min_length=1, max_length=50, description="Название места отдыха, длина от 1 до 50 символов")
    latitude: float = Field(..., ge=-90, le=90, description="Широта, число с плавающей точкой")
    longitude: float = Field(..., ge=-180, le=180, description="Долгота, число с плавающей точкой")
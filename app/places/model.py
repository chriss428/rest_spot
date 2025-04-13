from typing import List
from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database.base_model import Base
from app.users.model import User


class Place(Base):
    name: Mapped[str] = mapped_column(String(100), unique=True)
    latitude: Mapped[float]
    longitude: Mapped[float]

    user: Mapped[List["User"]] = relationship(
        secondary="user_place_assoc",
        back_populates="wish_places")

    def __str__(self):
        return (f"{self.__class__.__name__}("
                f"id={self.id}, "
                f"name={self.name!r},"
                f"latitude={self.latitude!r},"
                f"longitude={self.longitude!r}")

    def __repr__(self):
        return str(self)
from typing import List
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database.models.base import Base


class User_Place(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    place_id: Mapped[int] = mapped_column(ForeignKey("places.id"))

class User(Base):
    email: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[str] = mapped_column(String(150), unique=True)

    place: Mapped[List["Place"]] = relationship(
        secondary="user_places",
        back_populates="user")

    def __str__(self):
        return (f"{self.__class__.__name__}("
                f"id={self.id}, "
                f"full_name={self.full_name!r},"
                f"date_of_birth={self.date_of_birth!r},"
                f"email={self.email!r}")

    def __repr__(self):
        return str(self)

class Place(Base):
    name: Mapped[str] = mapped_column(String(100), unique=True)
    latitude: Mapped[float]
    longitude: Mapped[float]

    user: Mapped[List["User"]] = relationship(
        secondary="user_places",
        back_populates="place")

    def __str__(self):
        return (f"{self.__class__.__name__}("
                f"id={self.id}, "
                f"name={self.name!r},"
                f"latitude={self.latitude!r},"
                f"longitude={self.longitude!r}")

    def __repr__(self):
        return str(self)

from typing import List
from sqlalchemy import String, ForeignKey, text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database.base_model import Base
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.places.model import Place

class User(Base):
    email: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[str] = mapped_column(String(150), unique=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    is_user: Mapped[bool] = mapped_column(default=True, server_default=text('true'), nullable=False)
    is_admin: Mapped[bool] = mapped_column(default=False, server_default=text('false'), nullable=False)

    wish_places: Mapped[List["Place"]] = relationship(
        secondary="user_place_assoc",
        back_populates="user")

    def __str__(self):
        return (f"{self.__class__.__name__}("
                f"id={self.id}, "
                f"email={self.email!r}")

    def __repr__(self):
        return str(self)

class UserPlaceAssoc(Base):
    __tablename__ = "user_place_assoc"
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    place_id: Mapped[int] = mapped_column(ForeignKey("places.id"))
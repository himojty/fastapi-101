from typing import TYPE_CHECKING

from pydantic import EmailStr
from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import UserRelationMixin

if TYPE_CHECKING:
    from .article import Article
    from .profile import Profile
    from .item import Item


class User(Base):
    username: Mapped[str] = mapped_column(String(50), unique=True)
    # email: Mapped[EmailStr] = mapped_column(String(255), unique=True)
    # password_hash: Mapped[str] = mapped_column(String(512))

    articles: Mapped[list["Article"]] = relationship(back_populates="user")
    profile: Mapped["Profile"] = relationship(back_populates="user")
    items: Mapped[list["Item"]] = relationship(back_populates="user")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r})"

    def __repr__(self):
        return str(self)

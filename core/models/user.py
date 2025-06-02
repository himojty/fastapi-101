from typing import TYPE_CHECKING

from pydantic import EmailStr
from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import UserRelationMixin

if TYPE_CHECKING:
    from .article import Article
    from .profile import Profile


class User(UserRelationMixin, Base):
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[EmailStr] = mapped_column(String(255), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(512), nullable=False)

    articles: Mapped[list["Article"]] = relationship(back_populates="user")
    profile: Mapped["Profile"] = relationship(back_populates="user")

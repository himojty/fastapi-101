from typing import TYPE_CHECKING

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import UserRelationMixin

if TYPE_CHECKING:
    from .user import User


class Item(UserRelationMixin, Base):
    # _user_id_nullable = False
    # _user_id_unique = False
    _user_back_populates = "items"

    title: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )

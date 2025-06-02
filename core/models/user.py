from pydantic import EmailStr
from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[EmailStr] = mapped_column(String(255), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(512), nullable=False)

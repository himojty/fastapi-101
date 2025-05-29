from sqlalchemy.orm import Mapped

from .base import Base


class Article(Base):
    title: Mapped[str]
    content: Mapped[str]

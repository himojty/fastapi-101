from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from myapp.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[str] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(120))

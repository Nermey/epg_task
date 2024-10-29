from .database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import LargeBinary
from enum import Enum


class Sex(Enum):
    male = "male"
    female = "female"


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    surname: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    sex: Mapped[Sex]
    avatar: Mapped[bytes] = mapped_column(LargeBinary)


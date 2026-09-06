from uuid import UUID, uuid4
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base


class Skill(Base):
    __tablename__="skills"

    id: Mapped[UUID]=mapped_column(
        primary_key=True,
        default=uuid4
    )

    name: Mapped[str]=mapped_column(
        String(100),
        unique=True,
        index=True,
        nullable=False
    )

    description:Mapped[str|None]=mapped_column(
        String(500),
        nullable=True
    )
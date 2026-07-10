from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from ..database.database import Base

class Teste(Base):
    __tablename__ = "teste"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))
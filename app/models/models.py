from datetime import date
from sqlalchemy import String, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..database.database import Base


class Usuario(Base):
    __tablename__ = "usuario"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    senha: Mapped[str] = mapped_column(String(255), nullable=False)
    
    materias: Mapped[list["Materia"]] = relationship( 
        back_populates ="usuario"
    )


class Materia(Base):
    __tablename__ = "materia"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    materia: Mapped[str] = mapped_column(String(100), nullable=False)
    usuario_id: Mapped[int] = mapped_column(
        ForeignKey("usuario.id"),
        nullable=False
    )

    usuario: Mapped["Usuario"] = relationship(
        back_populates="materias"
    )
    sessoes: Mapped[list["SessaoEstudo"]] = relationship(
        back_populates="materia"
    )


class SessaoEstudo(Base):
    __tablename__ = "sessao_estudo"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    data: Mapped[date] = mapped_column(Date, nullable=False)
    horas: Mapped[float] = mapped_column(nullable=False)
    concluida: Mapped[bool] = mapped_column(default=False, nullable=False)
    
    materia_id: Mapped[int] = mapped_column(
        ForeignKey("materia.id"),
        nullable=False
    )

    materia: Mapped["Materia"] = relationship(
        back_populates="sessoes"
    )
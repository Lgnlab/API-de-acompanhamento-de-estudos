from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.schemas import MateriaCreate, MateriaResponse
from app.models.models import Usuario, Materia
from app.core.security import get_usuario_atual


router = APIRouter(prefix="/materias", tags=["Materias"])

@router.post("", response_model=MateriaResponse, status_code=status.HTTP_201_CREATED)
def cadastrar_materia(materia: MateriaCreate, usuario: Usuario = Depends(get_usuario_atual), db: Session = Depends(get_db)):
    nova_materia = Materia(materia=materia.materia, usuario_id=usuario.id)
    db.add(nova_materia)
    db.commit()
    db.refresh(nova_materia)

    return nova_materia

@router.get("", response_model=list[MateriaResponse])
def listar_materias(usuario: Usuario = Depends(get_usuario_atual), db: Session = Depends(get_db)):
    materias = (db.query(Materia).filter(Materia.usuario_id == usuario.id).all())
    
    return materias
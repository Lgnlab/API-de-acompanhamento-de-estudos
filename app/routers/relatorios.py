from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.database import get_db
from app.models.models import SessaoEstudo, Materia, Usuario
from app.schemas.schemas import RelatorioHorasMateriaResponse
from app.core.security import get_usuario_atual

router = APIRouter(prefix="/relatorios", tags=["Relatorios"])

@router.get("/horas-por-materia", response_model=list[RelatorioHorasMateriaResponse])
def horas_por_materia(usuario: Usuario = Depends(get_usuario_atual), db: Session = Depends(get_db)):
    relatorio = (db.query(Materia.materia, func.sum(SessaoEstudo.horas).label("total_horas")).join(Materia).filter(Materia.usuario_id == usuario.id).filter(SessaoEstudo.concluida == True).group_by(Materia.materia).all())

    return [RelatorioHorasMateriaResponse(materia=item.materia, total_horas=item.total_horas) for item in relatorio]
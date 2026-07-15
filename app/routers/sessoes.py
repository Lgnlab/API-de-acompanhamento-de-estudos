from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.models import SessaoEstudo, Materia, Usuario
from app.schemas.schemas import SessaoEstudoCreate, SessaoEstudoResponse
from app.core.security import get_usuario_atual

router = APIRouter(prefix="/sessoes", tags=["sessoes"])

@router.post("", response_model=SessaoEstudoResponse, status_code=status.HTTP_201_CREATED)
def cadastrar_sessao(sessao: SessaoEstudoCreate, usuario: Usuario = Depends(get_usuario_atual), db: Session = Depends(get_db)):
    materia = (db.query(Materia).filter(Materia.id == sessao.materia_id).first())
    if materia is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Matéria não encontrada.")
    if materia.usuario_id != usuario.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Você não tem permissão para acessar esta matéria.")
    
    nova_sessao = SessaoEstudo(data=sessao.data, horas=sessao.horas, concluida=sessao.concluida, materia_id=materia.id)
    
    db.add(nova_sessao)
    db.commit()
    db.refresh(nova_sessao)
    return nova_sessao

@router.get("", response_model=list[SessaoEstudoResponse])
def listar_sessoes(usuario: Usuario = Depends(get_usuario_atual), db: Session = Depends(get_db)):
    sessoes = (db.query(SessaoEstudo).join(Materia).filter(Materia.usuario_id == usuario.id).all())

    return sessoes  


@router.patch("/{sessao_id}", response_model=SessaoEstudoResponse)
def concluir_sessao(sessao_id: int, usuario: Usuario = Depends(get_usuario_atual), db: Session = Depends(get_db)):
    sessao = (db.query(SessaoEstudo).filter(SessaoEstudo.id == sessao_id).first())
    if sessao is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sessão não encontrada.")
    if sessao.materia.usuario_id != usuario.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Você não tem permissão para acessar esta sessão.")
    sessao.concluida = True
    if sessao.concluida:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Esta sessão já foi concluída.")
    
    sessao.concluida = True

    db.commit()
    db.refresh(sessao)

    return sessao
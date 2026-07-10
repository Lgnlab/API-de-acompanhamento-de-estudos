from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.schemas import UsuarioCreate, UsuarioResponse
from app.models.models import Usuario
from app.database.database import get_db
from app.core.security import gerar_hash_senha, verificar_senha


router = APIRouter(prefix="/autenticação", tags=["autenticação"])

@router.post("/cadastro", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def cadastrar_usuario(usuario: UsuarioCreate, db:Session = Depends(get_db)):
    usuario_existente = (db.query(Usuario).filter(Usuario.email == usuario.email)).first()
    if usuario_existente:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="E-mail já cadastrado.")
    
    senha_criptografada = gerar_hash_senha(usuario.senha)

    novo_usuario = Usuario(nome=usuario.nome, email=usuario.email, senha=senha_criptografada)

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario
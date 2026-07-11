from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.models import Usuario
from app.schemas.schemas import UsuarioCreate, LoginRequest
from app.core.security import gerar_hash_senha, verificar_senha


def cadastrar_usuario(db: Session, usuario: UsuarioCreate) -> Usuario:

    usuario_existente = (db.query(Usuario).filter(Usuario.email == usuario.email).first())

    if usuario_existente:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="E-mail já cadastrado.")

    senha_criptografada = gerar_hash_senha(usuario.senha)

    novo_usuario = Usuario(nome=usuario.nome, email=usuario.email, senha=senha_criptografada)

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario


def autenticar_usuario(db: Session, dados: LoginRequest):
    usuario = (db.query(Usuario)).filter(Usuario.email == dados.email).first()
    if usuario is None:
        raise HTTPException(status_code=401, detail="Email ou senha inválidos.")
    
    if not verificar_senha(dados.senha, usuario.senha):
        raise HTTPException(status_code=401, detail="Email ou senha inválidos.")
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.models import Usuario
from app.schemas.schemas import UsuarioCreate
from app.core.security import gerar_hash_senha


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
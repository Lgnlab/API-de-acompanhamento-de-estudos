from fastapi import APIRouter, Depends  , status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.schemas import UsuarioCreate, UsuarioResponse, TokenResponse, LoginRequest
from app.services.usuario_service import cadastrar_usuario, autenticar_usuario
from app.core.security import criar_token
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(prefix="/autenticacao", tags=["autenticacao"])

@router.post("/cadastro", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def criar_usuario(usuario: UsuarioCreate, db:Session = Depends(get_db)):
    return cadastrar_usuario(db, usuario)


@router.post("/login", response_model=TokenResponse)
def login(dados: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = autenticar_usuario(db, dados)
    token = criar_token({"sub": usuario.email})
    return TokenResponse(access_token=token, token_type="bearer")
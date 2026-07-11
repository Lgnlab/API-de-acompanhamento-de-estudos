from fastapi import APIRouter, Depends  , status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.schemas import UsuarioCreate, UsuarioResponse, TokenResponse, LoginRequest
from app.services.usuario_service import cadastrar_usuario


router = APIRouter(prefix="/autenticação", tags=["autenticação"])

@router.post("/cadastro", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def criar_usuario(usuario: UsuarioCreate, db:Session = Depends(get_db)):
    return cadastrar_usuario(db, usuario)


@router.post("/login", response_model=TokenResponse)
def login(dados: LoginRequest, db: Session = Depends(get_db)):
    ...
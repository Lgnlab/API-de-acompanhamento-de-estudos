from datetime import date
from pydantic import BaseModel, EmailStr, Field

class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr

    class Config:
        from_attributes = True


class MateriaCreate(BaseModel):
    materia: str

class MateriaResponse(BaseModel):
    id: int
    materia: str


    class Config:
        from_attributes = True
    

class SessaoEstudoCreate(BaseModel):
    data: date
    horas: float = Field(gt=0)
    concluida: bool = False


class SessaoEstudoResponse(BaseModel):
    id: int
    data: date
    horas: float
    concluida: bool

    class Config:
        from_attributes = True


class LoginRequest(BaseModel):
    email: EmailStr
    senha: str

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    token_type: str

    class Config:
        from_attributes = True
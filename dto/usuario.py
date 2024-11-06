from typing import Optional
from pydantic import BaseModel

class UsuarioDto(BaseModel):
    id: Optional[int] = None
    nombre: str
    edad: int
    role: str

class CreateUser(BaseModel):
    nombre: str
    edad: int


class UsuarioUpdateDTO(BaseModel):
    nombre: str
    edad: int
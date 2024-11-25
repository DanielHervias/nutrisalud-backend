from pydantic import BaseModel
from typing import Optional

class UsuarioDto(BaseModel):
    nombre: str
    edad: int
    role: str

class UsuarioCreateDto(BaseModel):
    nombre: str
    edad: int
    role: str

class UsuarioUpdateDto(BaseModel):
    nombre: Optional[str] = None
    edad: Optional[int] = None
    role: Optional[str] = None

from pydantic import BaseModel
from typing import Optional


class UsuarioDto(BaseModel):
    _id: Optional[str] = None
    name: str
    lastName: str
    email: str
    phone: str
    role: str
    fecha_nacimiento: str
    password: str
    talla: Optional[float] = None
    peso: Optional[float] = None
    experiencia: Optional[int] = None


class UsuarioCreateDto(BaseModel):
    name: str
    lastName: str
    email: str
    phone: str
    role: str
    fecha_nacimiento: str
    password: str
    talla: Optional[float] = None
    peso: Optional[float] = None
    experiencia: Optional[int] = None


class UsuarioUpdateDto(BaseModel):
    nombre: Optional[str] = None
    edad: Optional[int] = None
    role: Optional[str] = None


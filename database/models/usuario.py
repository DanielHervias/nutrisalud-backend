from typing import Optional
from pydantic import BaseModel


class Usuario(BaseModel):
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

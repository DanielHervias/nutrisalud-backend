from pydantic import BaseModel

class UsuarioDto(BaseModel):
    id: int
    nombre: str
    edad: str

class CreateUser(BaseModel):
    nombre: str
    edad: int


class UsuarioUpdateDTO(BaseModel):
    nombre: str
    edad: int
from typing import List, Optional
from pydantic import BaseModel

class HorarioDto(BaseModel):
    horaInicio: str
    horaFin: str
    date: str
    mes: str

class RegistrarHorario(BaseModel):
    horario: List[HorarioDto]

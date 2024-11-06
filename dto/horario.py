from typing import Optional
from pydantic import BaseModel

class HorarioDto(BaseModel):
    id: Optional[int] = None
    id_nutricionista: int
    mes: str
    dia: str
    fecha: str
    inicio: str
    fin: str

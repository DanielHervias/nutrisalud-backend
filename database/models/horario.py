from pydantic import BaseModel


class Horario(BaseModel):
    horaInicio: str
    horaFin: str
    date: str
    mes: str

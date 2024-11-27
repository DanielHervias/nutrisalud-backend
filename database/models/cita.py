from typing import Any
from pydantic import BaseModel


class Cita(BaseModel):
    nutritionist: str
    appointmentType: str
    date: str
    time: str
    report: Any 

from typing import Any
from pydantic import BaseModel


class CreateAppointmentDto(BaseModel):
    nutritionist_id: str
    patient_id: str
    nutritionist: str
    appointmentType: str
    date: str
    time: str
    report: Any

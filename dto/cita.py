from typing import Any, Optional
from pydantic import BaseModel


class CreateAppointmentDto(BaseModel):
    nutritionist_id: str
    patient_id: str
    appointment_type: str
    date: str
    time: str
    report: Optional[Any] = None

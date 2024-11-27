from typing import Any, Optional
from pydantic import BaseModel
from fastapi import File, UploadFile


class CreateAppointmentDto(BaseModel):
    nutritionist: str
    appointmentType: str
    date: str
    time: str
    report: Optional[UploadFile] = File(None)
    report_id: Any

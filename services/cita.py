import io

from fastapi import HTTPException

from dao.cita import CitaDao
from dto.cita import CreateAppointmentDto


class CitaService:
    async def crear_cita(createAppointmentDto: CreateAppointmentDto):
        
        return await CitaDao.crear_cita(createAppointmentDto)

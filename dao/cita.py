from fastapi import HTTPException
from database.initDatabase import citaDb
from dto.cita import CreateAppointmentDto


class CitaDao:
    async def obtener_cita(query):
        return await citaDb.find_one(query)
    
    async def crear_cita(createAppointmentDto: CreateAppointmentDto):
        nueva_cita = await citaDb.insert_one(createAppointmentDto.model_dump())
        return nueva_cita.acknowledged

        
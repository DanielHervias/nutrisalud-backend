from fastapi import HTTPException
from database.initDatabase import citaDb
from dto.cita import CreateAppointmentDto


class CitaDao:
    async def crear_cita(createAppointmentDto: CreateAppointmentDto):
        nueva_cita = await citaDb.insert_one(createAppointmentDto.model_dump())

        return {
            "message": "La Cita fue creada exitosamente.",
            "ok": nueva_cita.acknowledged,
        }
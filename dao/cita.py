from typing import List
from fastapi import HTTPException
from database.initDatabase import citaDb
from database.models.cita import Cita 
from dto.cita import CreateAppointmentDto


class CitaDao:
    async def obtener_cita(query):
        return await citaDb.find_one(query)
    
    async def crear_cita(createAppointmentDto: CreateAppointmentDto):
        nueva_cita = await citaDb.insert_one(createAppointmentDto.model_dump())
        return nueva_cita.acknowledged

    async def obtener_citas(query) -> List[Cita]:
        cursor = citaDb.find(query)
        print("cursor", cursor)
        citas = []
        async for cita in cursor:
            cita["_id"] = str(cita["_id"])
            cita["nutritionist_id"] = str(cita["nutritionist_id"])
            cita["patient_id"] = str(cita["patient_id"])
            citas.append(cita)
        return citas
        
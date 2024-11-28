from bson import ObjectId
from fastapi import HTTPException

from dao.cita import CitaDao
from dto.cita import CreateAppointmentDto


class CitaService:
    async def crear_cita(createAppointmentDto: CreateAppointmentDto):
        createAppointmentDto.nutritionist_id = ObjectId(
            createAppointmentDto.nutritionist_id
        )
        createAppointmentDto.patient_id = ObjectId(createAppointmentDto.patient_id)

        query = {
            "patient_id": createAppointmentDto.patient_id,
            "date": createAppointmentDto.date,
            "time": createAppointmentDto.time
        }
        cita = await CitaDao.obtener_cita(query)

        if cita:
            raise HTTPException(
                status_code=400, detail="Ya cuenta con una cita para esa hora"
            )

        query = {
            "nutritionist_id": createAppointmentDto.nutritionist_id,
            "date": createAppointmentDto.date,
            "time": createAppointmentDto.time
        }
        cita = await CitaDao.obtener_cita(query)

        if cita:
            raise HTTPException(
                status_code=400, detail="La fecha ya fue tomada por otro paciente"
            )

        cita = await CitaDao.obtener_cita(query)
        ok = await CitaDao.crear_cita(createAppointmentDto)

        return {
            "message": "La Cita fue creada exitosamente.",
            "ok": ok,
        }

    async def obtener_citas_usuario(patient_id: str):
        query = {
            "patient_id": ObjectId(patient_id)
        }
        return await CitaDao.obtener_citas(query)
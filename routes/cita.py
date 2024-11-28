from fastapi import APIRouter
from dto.cita import CreateAppointmentDto
from services.cita import CitaService

router = APIRouter()

@router.post("/cita")
async def crear_cita(createAppointmentDto: CreateAppointmentDto):
    return await CitaService.crear_cita(createAppointmentDto)

@router.get("/cita/usuario")
async def obtener_citas_usuario(patient_id: str):
    return await CitaService.obtener_citas_usuario(patient_id)
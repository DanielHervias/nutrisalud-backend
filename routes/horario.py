from fastapi import APIRouter
from dto.horario import RegistrarHorario
from services.horario import HorarioService

router = APIRouter()

@router.post("/horario")
async def crear_horario(horarios: RegistrarHorario):
    return await HorarioService.registrar_horario(horarios)


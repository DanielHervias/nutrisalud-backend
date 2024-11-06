from fastapi import APIRouter, Depends
from database.initDatabase import get_db
from dto.triaje import ObtenerTriajeDto, TriajeDto
from sqlalchemy.orm import Session
from services.triaje import TriajeService

router = APIRouter()

@router.post("/triaje")
def registrar_triaje(triaje: TriajeDto, db: Session = Depends(get_db)):
    return TriajeService.registrar_triaje(triaje, db)

@router.get("/triaje/paciente")
def obtener_triaje_paciente(body: ObtenerTriajeDto, db: Session = Depends(get_db)):
    return TriajeService.obtener_triaje_paciente(body.paciente_id, db)

@router.get("/triaje/medico")
def obtener_triaje_medico(body: ObtenerTriajeDto, db: Session = Depends(get_db)):
    return TriajeService.obtener_triaje_medico(body.medico_id, db)
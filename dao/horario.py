from typing import List
from fastapi import HTTPException
from database.models.horario import Horario
from dto.horario import HorarioDto
from sqlalchemy.orm import Session


class HorarioDao:
    def registrar_horario(horarios: List[HorarioDto], db: Session):
        db.bulk_insert_mappings(Horario, horarios)
        db.commit()
        return horarios
    
    def obtener_horario_nutricionista(id_nutricionista: int, db: Session):
        horarios = db.query(Horario).filter(Horario.id_nutricionista == id_nutricionista).all()
        return horarios

    """ def obtener_triaje_paciente(paciente_id: str, db: Session):
        horario = db.query(Triaje).filter(Triaje.paciente_id == paciente_id).first()
        if horario is None:
            raise HTTPException(
                status_code=404, detail="El usuario aún no tiene horario"
            )
        return horario
    
    def obtener_triaje_medico(medico_id: str, db: Session):
        horario = db.query(Triaje).filter(Triaje.medico_id == medico_id).all()
        if len(horario)==0:
            raise HTTPException(
                status_code=404, detail="El usuario aún no tiene horario"
            )
        return horario """

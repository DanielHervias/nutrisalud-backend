from typing import List
from fastapi import HTTPException
from database.models.horario import Horario
from dto.horario import HorarioDto


class HorarioDao:
    def registrar_horario(horarios: List[HorarioDto], db: Session):
        db.bulk_insert_mappings(Horario, horarios)
        db.commit()
        return horarios
    
    def obtener_horario_nutricionista(id_nutricionista: int, db: Session):
        horarios = db.query(Horario).filter(Horario.id_nutricionista == id_nutricionista).all()
        return horarios

from fastapi import HTTPException
from database.models.triaje import Triaje
from dto.triaje import TriajeDto
from sqlalchemy.orm import Session


class TriajeDao:
    def registrar_triaje(triaje: TriajeDto, db: Session):
        nuevo_triaje = Triaje(
            historial_medico_archivo=triaje.historial_medico_archivo,
            paciente_id=triaje.paciente_id,
            medico_id=triaje.medico_id,
            sintomas=triaje.sintomas,
            habitos_alimenticios=triaje.habitos_alimenticios,
            alimentos_favoritos=triaje.alimentos_favoritos,
            alimentos_no_tolerados=triaje.alimentos_no_tolerados,
            objetivo_perder_peso=triaje.objetivo_perder_peso,
            objetivo_ganar_masa_muscular=triaje.objetivo_ganar_masa_muscular,
            objetivo_otro=triaje.objetivo_otro,
        )
        db.add(nuevo_triaje)
        db.commit()
        db.refresh(nuevo_triaje)
        return nuevo_triaje

    def obtener_triaje_paciente(paciente_id: str, db: Session):
        triaje = db.query(Triaje).filter(Triaje.paciente_id == paciente_id).first()
        if triaje is None:
            raise HTTPException(
                status_code=404, detail="El usuario aún no tiene triaje"
            )
        return triaje
    
    def obtener_triaje_medico(medico_id: str, db: Session):
        triaje = db.query(Triaje).filter(Triaje.medico_id == medico_id).all()
        if len(triaje)==0:
            raise HTTPException(
                status_code=404, detail="El usuario aún no tiene triaje"
            )
        return triaje

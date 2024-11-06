from dao.horario import HorarioDao
from dto.horario import HorarioDto
from typing import List

class HorarioService:
    def registrar_horario_particular(horario: HorarioDto, db):
        return HorarioDao.registrar_horario(list([horario]), db)
    
    def registrar_horario_mensual(id_nutricionista: int, db):
        return HorarioDao.obtener_horario_nutricionista(id_nutricionista, db)
    
    def obtener_horario_mensual(id_nutricionista, db):
        return HorarioDao.obtener_horario_nutricionista(id_nutricionista, db)
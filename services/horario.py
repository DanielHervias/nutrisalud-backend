from dao.horario import HorarioDao
from dto.horario import HorarioDto

class HorarioService:
    async def registrar_horario(horario: HorarioDto):
        return await HorarioDao.registrar_horario(list([horario]))

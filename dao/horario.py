from typing import List
from fastapi import HTTPException
from database.initDatabase import horarioDb
from dto.horario import HorarioDto


class HorarioDao:
    async def registrar_horario(horarios: List[HorarioDto]):
        horarios_dumped = [horario.model_dump() for horario in horarios]
        response = await horarioDb.insert_many(horarios_dumped)
        print("response2", response)
        return response.inserted_ids  
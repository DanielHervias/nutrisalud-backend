# from fastapi import APIRouter, Depends
# from database.initDatabase import get_db
# from dto.horario import HorarioDto
# from services.horario import HorarioService

# router = APIRouter()

# @router.post("/horario/particular")
# def registrar_horario_particular(horario: HorarioDto, db: Session = Depends(get_db)):
#     return HorarioService.registrar_horario_particular(horario, db)

# """ @router.post("/horario/mensual")
# def obtener_triaje_paciente(body: ObtenerTriajeDto, db: Session = Depends(get_db)):
#     return HorarioService.obtener_triaje_paciente(body.paciente_id, db)
# """
# @router.get("/horario/{id_nutricionista}")
# def obtener_triaje_medico(id_nutricionista: int, db: Session = Depends(get_db)):
#     return HorarioService.obtener_horario_mensual(id_nutricionista, db) 

# """ 
# DISPONIBILIDAD_NUTRICIONISTA
# {
#   "id_nutricionista": "id_nutri",
#   "mes": "junio",
#   "disponibilidad": [
#     {
#       "dia": "miércoles",
#       "fecha": "2024-06-05",
#       "intervalos": [
#         {
#           "inicio": "12:00",
#           "fin": "18:30"
#         }
#       ]
#     }
#   ]
# }

# De esa forma solo si es para un dia en particular

# DISPONIBILIDAD_NUTRICIONISTA

# {
#   "id_nutricionista": "id_nutri",
#   "mes": "junio",
#   "disponibilidad": [
#     {
#       "dia": "miércoles",
#       "intervalos": [
#         {
#           "inicio": "12:00",
#           "fin": "18:30"
#         }
#       ]
#     }
#   ]
# }
# Así si es para los miercoles de todo el mes
# """





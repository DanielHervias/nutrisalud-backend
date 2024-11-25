# from fastapi import APIRouter
# from dto.triaje import ObtenerTriajeDto, TriajeDto
# from services.triaje import TriajeService

# router = APIRouter()

# @router.post("/triaje")
# def registrar_triaje(triaje: TriajeDto):
#     return TriajeService.registrar_triaje(triaje)

# @router.get("/triaje/paciente")
# def obtener_triaje_paciente(body: ObtenerTriajeDto):
#     return TriajeService.obtener_triaje_paciente(body.paciente_id)

# @router.get("/triaje/medico")
# def obtener_triaje_medico(body: ObtenerTriajeDto):
#     return TriajeService.obtener_triaje_medico(body.medico_id)
from fastapi import APIRouter
from dto.usuario import UsuarioCreateDto, UsuarioUpdateDto
from services.usuario import UsuarioService

router = APIRouter()

@router.post("/usuario")
async def crear_usuario(usuario_nuevo: UsuarioCreateDto):
    return await UsuarioService.crear_usuario(usuario_nuevo)

@router.put("/usuario/{usuario_id}")
async def actualizar_usuario(usuario_id: str, body: UsuarioUpdateDto):
    return await UsuarioService.actualizar_usuario(usuario_id, body)
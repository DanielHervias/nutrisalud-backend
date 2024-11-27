from fastapi import APIRouter
from dto.usuario import UsuarioCreateDto, UsuarioUpdateDto, UserLoginDto
from services.usuario import UsuarioService

router = APIRouter()

@router.post("/usuario")
async def create_user(usuario_nuevo: UsuarioCreateDto):
    return await UsuarioService.crear_usuario(usuario_nuevo)

@router.get("/usuario/login")
async def login_user(body: UserLoginDto):
    return await UsuarioService.user_login(body)

""" @router.put("/usuario/{usuario_id}")
async def actualizar_usuario(usuario_id: str, body: UsuarioUpdateDto):
    return await UsuarioService.actualizar_usuario(usuario_id, body) """
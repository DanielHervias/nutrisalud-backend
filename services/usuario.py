from dao.usuario import UsuarioDao
from dto.usuario import UsuarioCreateDto, UsuarioUpdateDto

class UsuarioService:
    async def crear_usuario(usuario_nuevo: UsuarioCreateDto):
        return await UsuarioDao.crear_usuario(usuario_nuevo)
    
    async def actualizar_usuario(usuario_id, body: UsuarioUpdateDto):
        return await UsuarioDao.actualizar_usuario(usuario_id, body)
from dao.usuario import UsuarioDao
from dto.usuario import UsuarioCreateDto, UsuarioDto, UserLoginDto

class UsuarioService:
    async def crear_usuario(usuario_nuevo: UsuarioCreateDto):
        return await UsuarioDao.crear_usuario(usuario_nuevo)
    
    async def user_login(body: UserLoginDto ):
        email, password = body.email, body.password
        user: UsuarioDto = await UsuarioDao.get_user_by_email(email)

        if (user.password == password):
            return {"ok": True}
        else:
            return {"ok": False}
from dao.usuario import UsuarioDao
from dto.usuario import UsuarioCreateDto, UsuarioDto

class UsuarioService:
    async def crear_usuario(usuario_nuevo: UsuarioCreateDto):
        return await UsuarioDao.crear_usuario(usuario_nuevo)
    
    async def user_login(email: str, password: str ):
        user = await UsuarioDao.get_user_by_email(email)

        if (user["password"] == password):
            user["_id"] = str(user["_id"])
            del user["password"]
            return {"ok": True, "user": user}
        else:
            return {"ok": False}
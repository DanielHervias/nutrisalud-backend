from fastapi import HTTPException

from dao.usuario import UsuarioDao
from dto.usuario import UsuarioCreateDto

class UsuarioService:
    async def crear_usuario(usuario_nuevo: UsuarioCreateDto):
        return await UsuarioDao.crear_usuario(usuario_nuevo)
    
    async def user_login(email: str, password: str ):
        user = await UsuarioDao.get_user_by_email(email)
        if user is None:
            raise HTTPException(status_code=404, detail="Email o contraseña incorrectos.")

        if (user["password"] == password):
            user["_id"] = str(user["_id"])
            del user["password"]
            return {"ok": True, "user": user}
        else:
            return {"ok": False}
        
    async def obtener_especialistas(role: str):
        return await UsuarioDao.get_user_by_role(role)
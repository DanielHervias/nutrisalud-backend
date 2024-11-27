from bson import ObjectId
from fastapi import HTTPException
from database.initDatabase import usuarioDb
from dto.usuario import UsuarioCreateDto, UsuarioUpdateDto, UsuarioDto


class UsuarioDao:
    async def crear_usuario(usuario_nuevo: UsuarioCreateDto):
        usuario = await usuarioDb.find_one({"email": usuario_nuevo.email})

        if usuario:
            raise HTTPException(status_code=400, detail="El usuario ya existe")

        nuevo_usuario = await usuarioDb.insert_one(usuario_nuevo.model_dump())

        return {
            "message": "Usuario creado exitosamente.",
            "ok": nuevo_usuario.acknowledged,
        }
    
    async def get_user_by_email(email: str) -> UsuarioDto:
        user = await usuarioDb.find_one({"email": email})
        if user is None:
            raise HTTPException(status_code=404, detail="Email o contraseña incorrectos.")
        return user

    async def actualizar_usuario(
        usuario_id: str, usuario_actualizado: UsuarioUpdateDto
    ):
        usuario = await usuarioDb.find_one({"_id": ObjectId(usuario_id)})

        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        # Filtrar solo los campos que fueron enviados para actualizar
        update_fields = usuario_actualizado.model_dump(
            exclude_unset=True
        )  # Esto ignora campos no proporcionados

        if not update_fields:
            raise HTTPException(
                status_code=400, detail="No se proporcionaron datos para actualizar"
            )

        result = await usuarioDb.update_one(
            {"_id": ObjectId(usuario_id)},
            {"$set": update_fields},
        )

        if result.modified_count == 0:
            raise HTTPException(status_code=400, detail="No se realizaron cambios")

        return {"message": "Usuario actualizado exitosamente."}

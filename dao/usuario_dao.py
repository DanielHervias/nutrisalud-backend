from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.initDatabase import get_db
from sql_models.usuario import Usuario
from dto.usuario import CreateUser, UsuarioDto, UsuarioUpdateDTO

router = APIRouter()

@router.post("/usuario")
def crear_usuario(usuario: CreateUser, db: Session = Depends(get_db)):
    nuevo_usuario = Usuario(nombre=usuario.nombre, edad=usuario.edad)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

@router.get("/usuario/{usuario_id}")
def leer_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.get("/usuarios")
def leer_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    if usuarios is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuarios

@router.put("/usuario/{usuario_id}")
def actualizar_usuario(usuario_id: int, usuario: UsuarioUpdateDTO, db: Session = Depends(get_db)):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()

    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db_usuario.edad = usuario.edad
    db_usuario.nombre = usuario.nombre

    db.commit()
    db.refresh(db_usuario)
    return db_usuario

@router.delete("/usuario/{usuario_id}")
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario_a_eliminar = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario_a_eliminar:
        db.delete(usuario_a_eliminar)
        db.commit()
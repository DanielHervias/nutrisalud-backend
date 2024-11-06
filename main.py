from fastapi import FastAPI
from database.initDatabase import engine, Base
from dao import usuario_dao  # Importa el router de usuarios

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluir las rutas del router de usuarios
app.include_router(usuario_dao.router, tags=["usuario"])

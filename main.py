from fastapi import FastAPI
from database.initDatabase import engine, Base
from routes import triaje_controller, usuario_rt

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluir las rutas del router de usuarios
app.include_router(usuario_rt.router, tags=["usuario"])
app.include_router(triaje_controller.router, tags=["triaje"])
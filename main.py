from dotenv import load_dotenv

from fastapi import FastAPI
from contextlib import asynccontextmanager
from routes import triaje_controller, usuario, horario_api

load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting FastAPI with MongoDB...")
    yield
    print("Shutting down FastAPI...")


app = FastAPI(lifespan=lifespan)

# Incluir las rutas del router de usuarios
app.include_router(usuario.router, tags=["usuario"])
# app.include_router(triaje_controller.router, tags=["triaje"])
# app.include_router(horario_api.router, tags=["horario"])

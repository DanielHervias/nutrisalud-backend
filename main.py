from dotenv import load_dotenv

from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from routes import cita, horario, usuario

load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting FastAPI with MongoDB...")
    yield
    print("Shutting down FastAPI...")

origins = [
    "http://localhost:5173",
]


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir solo los orígenes especificados
    allow_credentials=True,  # Permitir cookies o credenciales
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

app.include_router(usuario.router, tags=["usuario"])
app.include_router(cita.router, tags=["cita"])
app.include_router(horario.router, tags=["horario"])
# app.include_router(triaje_controller.router, tags=["triaje"])

import os

from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = f"mongodb+srv://{os.getenv("MONGO_USER_NAME")}:{os.getenv("MONGO_USER_PASSWORD")}@cluster0.pk30t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# MONGO_URL = "mongodb://localhost:27017"
mongo_client = AsyncIOMotorClient(MONGO_URL)
database = mongo_client["nutrisalud"]

usuarioDb = database["usuario"]
citaDb = database["cita"]
horarioDb = database["horario"]



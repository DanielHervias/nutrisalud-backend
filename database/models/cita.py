from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database.initDatabase import Base


class Cita(Base):
    __tablename__ = "cita"

    id = Column(Integer, primary_key=True, index=True)
    id_nutricionista = Column(Integer, ForeignKey("usuario.id"), index=True)
    id_paciente = Column(Integer, ForeignKey("usuario.id"), index=True)
    nombre_archivo = Column(String, nullable=False)
    tipo_archivo = Column(String, nullable=False)
    data = Column(String, nullable=False)
    seguimiento = Column(Boolean, nullable=False)  
    primera_visita = Column(Boolean, nullable=False)
    fecha = Column(String, nullable=False)
    hora = Column(String, nullable=False)

    def __repr__(self):
        return f"<Cita(id={self.id})>"

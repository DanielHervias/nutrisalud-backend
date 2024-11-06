from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.initDatabase import Base


class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    edad = Column(Integer, nullable=False)
    role = Column(String, nullable=False)  # Esto indica si es 'paciente' o 'medico'

    triajes = relationship(
        "Triaje", back_populates="paciente", foreign_keys="[Triaje.paciente_id]"
    )
    triajes_medico = relationship(
        "Triaje", back_populates="medico", foreign_keys="[Triaje.medico_id]"
    )

    def __repr__(self):
        return f"<Usuario(id={self.id}, nombre='{self.nombre}', edad={self.edad}, role='{self.role}')>"

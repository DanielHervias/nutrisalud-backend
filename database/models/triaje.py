from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from database.initDatabase import Base


class Triaje(Base):
    __tablename__ = "triaje"

    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("usuario.id"), index=True)
    medico_id = Column(Integer, ForeignKey("usuario.id"), index=True)
    historial_medico_archivo = Column(String, nullable=True)
    sintomas = Column(String, nullable=True)
    habitos_alimenticios = Column(String, nullable=True)
    alimentos_favoritos = Column(String, nullable=True)
    alimentos_no_tolerados = Column(String, nullable=True)
    objetivo_perder_peso = Column(Boolean, nullable=True)
    objetivo_ganar_masa_muscular = Column(Boolean, nullable=True)
    objetivo_otro = Column(String, nullable=True)

    # Relación con paciente: usamos primaryjoin para indicar cómo hacer la unión
    paciente = relationship(
        "Usuario",
        back_populates="triajes",
        foreign_keys=[paciente_id],
        primaryjoin="Triaje.paciente_id == Usuario.id",  # Condición de unión explícita
    )

    # Relación con medico: usamos primaryjoin para indicar cómo hacer la unión
    medico = relationship(
        "Usuario",
        back_populates="triajes_medico",
        foreign_keys=[medico_id],
        primaryjoin="Triaje.medico_id == Usuario.id",  # Condición de unión explícita
    )

    def __repr__(self):
        return f"<Triaje(id={self.id})>"

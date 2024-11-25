from pydantic import BaseModel


class Triaje(BaseModel):
    __tablename__ = "triaje"


# id = Column(Integer, primary_key=True, index=True)
# paciente_id = Column(Integer, ForeignKey("usuario.id"), index=True)
# medico_id = Column(Integer, ForeignKey("usuario.id"), index=True)
# historial_medico_archivo = Column(String, nullable=True)
# sintomas = Column(String, nullable=True)
# habitos_alimenticios = Column(String, nullable=True)
# alimentos_favoritos = Column(String, nullable=True)
# alimentos_no_tolerados = Column(String, nullable=True)
# objetivo_perder_peso = Column(Boolean, nullable=True)
# objetivo_ganar_masa_muscular = Column(Boolean, nullable=True)
# objetivo_otro = Column(String, nullable=True)

# def __repr__(self):
#     return f"<Triaje(id={self.id})>"

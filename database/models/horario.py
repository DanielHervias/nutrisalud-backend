from sqlalchemy import Column, ForeignKey, Integer, String
from database.initDatabase import Base


class Horario(Base):
    __tablename__ = "horario"

    id = Column(Integer, primary_key=True, index=True)
    id_nutricionista = Column(Integer, ForeignKey("usuario.id"), index=True)
    mes = Column(String, nullable=False)
    dia = Column(String, nullable=False)
    fecha = Column(String, nullable=False)  # Esto indica si es 'paciente' o 'medico'
    inicio = Column(String, nullable=False)
    fin = Column(String, nullable=False)

    def __repr__(self):
        return f"<Horario(id={self.id})>"

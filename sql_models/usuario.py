from sqlalchemy import Column, Integer, String
from database.initDatabase import Base

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    edad = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Usuario(id={self.id}, nombre='{self.nombre}', edad={self.edad})>"

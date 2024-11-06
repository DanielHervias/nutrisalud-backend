from typing import Optional
from pydantic import BaseModel

class TriajeDto(BaseModel):
    id: Optional[int] = None
    paciente_id: Optional[int] = None
    medico_id: Optional[int] = None
    historial_medico_archivo: Optional[str] = None  
    sintomas: Optional[str] = None                  
    habitos_alimenticios: Optional[str] = None      
    alimentos_favoritos: Optional[str] = None       
    alimentos_no_tolerados: Optional[str] = None    
    objetivo_perder_peso: Optional[bool] = None     
    objetivo_ganar_masa_muscular: Optional[bool] = None  
    objetivo_otro: Optional[str] = None   

class ObtenerTriajeDto(BaseModel):
    paciente_id: Optional[int] = None
    medico_id: Optional[int] = None

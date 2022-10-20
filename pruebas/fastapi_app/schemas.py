"""coding=utf-8."""
 
from datetime import date
from typing import List, Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    id_usuario : Optional[int]
    nombre_usuario : str
    apellido_paterno : str
    apellido_materno : str
    email : str
    tipo_usuario : str

class CicloEscolarBase(BaseModel):
    id_ciclo_escolar : Optional[int]
    periodo : str
    anio : int
    registro_grupos_inicio : date
    registro_grupos_termino : date
    registro_disponibilidad_inicio : date
    registro_disponibilidad_termino : date
    registro_contrataciones_inicio : date
    registro_contrataciones_termino : date
    registro_horarios_secretaria_inicio : date
    registro_horarios_secretaria_termino : date
    registro_aprobacion_coordi_docente_inicio : date
    registro_aprobacion_coordi_docente_termino : date
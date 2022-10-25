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

class WOIUserBase(BaseModel): 
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

class WOICicloEscolarBase(BaseModel):
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

class WOICarrerasBase(BaseModel):
    nombre_carrera : str
    coordinador_carrera : int

class CarrerasBase(BaseModel):
    id_carrera : Optional[int]
    nombre_carrera : str
    coordinador_carrera : int

class PlanEstudiosBase(BaseModel):
    id_materia : Optional[int]
    nombre_materia : str
    cuatrimestre : int
    total_horas : int
    total_horas_semana : int
    carrera : int

class WOIPlanEstudiosBase(BaseModel):
    
    nombre_materia : str
    cuatrimestre : int
    total_horas : int
    total_horas_semana : int
    carrera : int

class TurnosBase(BaseModel):
    id_turno : Optional[int]
    nombre_turno : str
    hora_entrada : str
    hora_salida : str


class WOITurnosBase(BaseModel):
    nombre_turno : str
    hora_entrada : str
    hora_salida : str
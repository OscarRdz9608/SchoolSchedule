from sqlite3 import Date
import databases

from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import create_engine 
from sqlalchemy import MetaData 
from sqlalchemy import select, insert, update, delete

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

DATABASE_URL = "sqlite:///clientes.db"

metadata =MetaData()

user_type= Table(
    'user_type', metadata,
    Column('user_type', Integer, primary_key=True),
)
usuario= Table(
    'usuarios', metadata,
    Column('id_usuario', Integer, primary_key=True),
    Column('nombre_usuario', String),
    Column('apellido_paterno', String),
    Column('apellido_materno', String),
    Column('email', String),
    Column('tipo_usuario', Integer),
)

periodos= Table(
    'periodos', metadata,
    Column('periodos', Integer, primary_key=True),
)
ciclo_escolar= Table(
    'ciclo_escolar', metadata,
    Column('id_ciclo_escolar', Integer, primary_key=True),
    Column('anio', Integer),
    Column('registro_grupos_inicio', Date),
    Column('registro_grupos_termino', Date),
    Column('registro_disponibilidad_inicio', Date),
    Column('registro_disponibilidad_termino', Date),  
    Column('registro_contrataciones_inicio', Date),
    Column('registro_contrataciones_termino', Date),
    Column('registro_horarios_secretaria_inicio', Date),
    Column('registro_horarios_secretaria_termino', Date),  
    Column('registro_aprobacion_coordi_docente_inicio', Date),
    Column('registro_aprobacion_coordi_docente_termino', Date)
)

plan_estudios= Table(
    'plan_estudios', metadata,
    Column('id_materia', Integer, primary_key=True),
    Column('nombre_materia', String),
    Column('cuatrimestre', Integer),
    Column('total_horas', Integer),
    Column('carrera', Integer),
)


turnos= Table(
    'turnos', metadata,
    Column('id_turno', Integer, primary_key=True),
    Column('nombre_turno', String),
    Column('hora_entrada', Date),
    Column('hora_salida', Date)
)



database = databases.Database(DATABASE_URL)

engine = create_engine(DATABASE_URL)

metadata.create_all(engine)

class user_type(BaseModel):
    user_type:int


class usuario(BaseModel):
    id_usuario: int
    nombre_usuario: str
    apellido_paterno: str
    apellido_materno: str
    email: str
    tipo_usuario: int

class periodos(BaseModel):
    periodos: int


class ciclo_escolar(BaseModel):
    id_ciclo_escolar: int
    registro_grupos_inicio: Date
    registro_grupos_termino: Date
    registro_disponibilidad_inicio: Date
    registro_disponibilidad_termino: Date
    registro_contrataciones_inicio: Date
    registro_contrataciones_termino: Date
    registro_horarios_secretaria_inicio: Date
    registro_horarios_secretaria_termino: Date
    registro_aprobacion_coordi_docente_inicio: Date
    registro_aprobacion_coordi_docente_termino: Date

class plan_estudios(BaseModel):
    id_materia: int
    nombre_materia: str
    cuatrimestre: int
    total_horas: int
    carrera: int

class turnos(BaseModel):
    id_turno: int
    nombre_turno: str
    hora_entrada: Date
    hora_salida: Date



class Message(BaseModel):
    message: str

app= FastAPI()


@app.get("/", response_model=Message)
async def root():
    return {"message": "Hello World"}

#USUARIOS 

@app.get("/usuarios", response_model=List[usuario],
    summary="Obtener un listado de usuarios",
    description="Obtener un listado de usuarios", 
    tags=["usuario"])
async def get_user():
    query = select(usuario)
    return await database.fetch_all(query)

@app.get("/usuario/{id_usuario}",  response_model=usuario,
    summary="Obtener un listado de un usuario",
    description="Obtener un listado un de usuario", 
    tags=["usuario"])
async def get_cliente (id_usuario=int):
    query = select(usuario).where(usuario.c.id_cliente == id_usuario)
    return await database.fetch_one(query)

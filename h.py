from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, create_engine, inspect, SmallInteger, Date, Time

Base = declarative_base()
engine = create_engine('postgresql://postgres:12345678@localhost:5432/horarios') #CONEXIÓN

q = engine.execute('''SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog' AND 
    schemaname != 'information_schema';''')
available_tables = q.fetchall()
#print(available_tables)

class Usuarios(Base):
    tablename = 'usuarios'

    id_usuario = Column(Integer(), primary_key = True)
    nombre_usuario = Column(String(20), nullable = False)
    apellido_paterno = Column(String(15), nullable = False)
    apellido_materno = Column(String(15), nullable = False)
    email = Column(String(60), nullable = False)
    tipo_usuario = Column(String(1), nullable = False)

class CicloEscolar(Base):
    tablename = 'ciclo_escolar'

    id_ciclo_escolar = Column(Integer(), primary_key = True)
    periodo = Column(String(1), nullable = False)
    anio = Column(SmallInteger())
    registro_grupos_inicio = Column(Date(), nullable = False)
    registro_grupos_termino = Column(Date(), nullable = False)
    registro_disponibilidad_inicio = Column(Date(), nullable = False)
    registro_disponibilidad_termino = Column(Date(), nullable = False)
    registro_contrataciones_inicio = Column(Date(), nullable = False)
    registro_contrataciones_termino = Column(Date(), nullable = False)
    registro_horarios_secretaria_inicio = Column(Date(), nullable = False)
    registro_horarios_secretaria_termino = Column(Date(), nullable = False)
    registro_aprobacion_coordi_docente_inicio = Column(Date(), nullable = False)
    registro_aprobacion_coordi_docente_termino = Column(Date(), nullable = False)

class Carreras(Base):
    tablename = 'carreras'

    id_carrera = Column(Integer(), primary_key = True)
    nombre_carrera = Column(String(60), nullable = False)
    coordinador = Column(Integer(), nullable = False)

class PlanEstudios(Base):
    tablename = 'plan_estudios'

    id_materia = Column(Integer(), primary_key = True)
    nombre_materia = Column(String(60), nullable = False)
    cuatrimestre = Column(SmallInteger(), nullable = False)
    total_horas = Column(SmallInteger(), nullable = False)
    total_horas_semana = Column(SmallInteger(), nullable = False)
    carrera = Column(SmallInteger(), nullable = False)

class Turnos(Base):
    tablename = 'turnos'
    id_turno = Column(Integer(), primary_key = True)
    nombre_turno = Column(String(15), nullable = False)
    hora_entrada = Column(Time())
    hora_salida = Column(Time())

Session = sessionmaker(engine)
session = Session()


#Insertar usuario
def insert_row_Usuarios(nombre_usuario, apellido_paterno, apellido_materno, email, tipo_usuario):
        try:
            user = Usuarios(nombre_usuario = nombre_usuario, apellido_paterno = apellido_paterno,
                apellido_materno = apellido_materno, email = email, tipo_usuario = tipo_usuario)
            session.add(user)
            session.commit()
            return True
        except Exception as error:
            print(error)
            return False

#Consultar
def query_row_Usuarios(email: str):
    try:
        user = session.query(Usuarios.id_usuario,Usuarios.nombre_usuario, Usuarios.apellido_paterno, Usuarios.apellido_materno, Usuarios.email, Usuarios.tipo_usuario).filter(
            Usuarios.email == email
        ).first()
        if user:
                return dict(user)
        else:
                return None
    except Exception as error:
        print(error)
        return None

#Actualizar
def update_row_Usuarios(id_usuario, nombre_usuario, apellido_paterno, apellido_materno, email, tipo_usuario):
    try:
        session.query(Usuarios).filter(
                Usuarios.id_usuario == id_usuario 
        ).update(
                {
                        Usuarios.nombre_usuario : nombre_usuario,
                        Usuarios.apellido_paterno : apellido_paterno,
                        Usuarios.apellido_materno : apellido_materno,
                        Usuarios.email : email,
                        Usuarios.tipo_usuario : tipo_usuario,
                }
        )
        session.commit()
        return True
    except Exception as error:
        print(error)
        return False

#Eliminar
def delete_row_Usuarios(email: str):
    try:
        session.query(Usuarios).filter(
                Usuarios.email == email
        ).delete()
        session.commit()
        return True
    except Exception as error:
        print(error)
        return False



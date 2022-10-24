import enum
from sqlalchemy import Column, Integer, String, SmallInteger, Date, Time, create_engine, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine("postgresql://postgres:26Ti9228twc8!d3@db.svhulthwokfuuwlasvul.supabase.co:5432/postgres")

class TipoUsuario(enum.Enum):
    administrador = 1
    secretario_academico = 2
    coordinador_academico = 3
    coordinador_idiomas = 4
    docente = 5

class Usuarios(Base):
    __tablename__ = 'usuarios'

    id_usuario = Column(Integer(), primary_key = True)
    nombre_usuario = Column(String(20), nullable = False)
    apellido_paterno = Column(String(15), nullable = False)
    apellido_materno = Column(String(15), nullable = False)
    email = Column(String(60), nullable = False, unique = True)
    tipo_usuario = Column(String(5), nullable = False)

class CicloEscolar(Base):
    __tablename__ = 'ciclo_escolar'

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

Session = sessionmaker(engine)
session = Session()

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

if __name__=='__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print(insert_row_Usuarios(nombre_usuario="José Luis", apellido_paterno="Escobar", apellido_materno="Perez", email="1719110043@utectulancingo.edu.mx", tipo_usuario="1"))
    tipo = query_row_Usuarios(email="1719110043@utectulancingo.edu.mx")
    print(tipo)
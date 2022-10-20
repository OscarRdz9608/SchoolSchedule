from enum import unique
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, create_engine, SmallInteger, Date, Time

Base = declarative_base()
engine = create_engine('postgresql://postgres:12345678@localhost:5432/horarios') #CONEXIÓN

#q = engine.execute('''SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';''')
#available_tables = q.fetchall()
#print(available_tables)

class Usuarios(Base):
    __tablename__ = 'usuarios'

    id_usuario = Column(Integer(), primary_key = True)
    nombre_usuario = Column(String(20), nullable = False)
    apellido_paterno = Column(String(15), nullable = False)
    apellido_materno = Column(String(15), nullable = False)
    email = Column(String(60), nullable = False)
    tipo_usuario = Column(String(1), nullable = False)

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

class Carreras(Base):
    __tablename__ = 'carreras'

    id_carrera = Column(Integer(), primary_key = True)
    nombre_carrera = Column(String(60), nullable = False)
    coordinador_carrera = Column(Integer(), nullable = False)

class PlanEstudios(Base):
    __tablename__ = 'plan_estudios'

    id_materia = Column(Integer(), primary_key = True)
    nombre_materia = Column(String(60), nullable = False)
    cuatrimestre = Column(SmallInteger(), nullable = False)
    total_horas = Column(SmallInteger(), nullable = False)
    total_horas_semana = Column(SmallInteger(), nullable = False)
    carrera = Column(SmallInteger(), nullable = False)

class Turnos(Base):
    __tablename__ = 'turnos'
    id_turno = Column(Integer(), primary_key = True)
    nombre_turno = Column(String(15), nullable = False)
    hora_entrada = Column(Time())
    hora_salida = Column(Time())

Session = sessionmaker(engine)
session = Session()

#################################################   USUARIOS
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

'''if insert_row_Usuarios(nombre_usuario = "Juan", apellido_paterno = "López", apellido_materno = "Pérez", 
    email = "1719110050@utectulancingo.edu.mx", tipo_usuario = '1') is True:
    print("Usuario creado")'''

'''print(update_row_Usuarios(id_usuario = 8, nombre_usuario = "Benajmín", apellido_paterno = "García", apellido_materno = "Pérez", 
    email = "1719110050@utectulancingo.edu.mx", tipo_usuario = '1'))'''
#print(query_row_Usuarios(id_usuario = 1))

#print(query_row_Usuarios(email = "1719110050@utectulancingo.edu.mx"))


#################################################### CICLO ESCOLAR

def insert_row_ciclo_escolar(periodo, anio, registro_grupos_inicio, registro_grupos_termino, registro_disponibilidad_inicio,
registro_disponibilidad_termino, registro_contrataciones_inicio, registro_contrataciones_termino, registro_horarios_secretaria_inicio,
registro_horarios_secretaria_termino, registro_aprobacion_coordi_docente_inicio, registro_aprobacion_coordi_docente_termino):
    try:
        ciclo_escolar = CicloEscolar(periodo = periodo, anio = anio, registro_grupos_inicio = registro_grupos_inicio, 
        registro_grupos_termino = registro_grupos_termino, registro_disponibilidad_inicio = registro_disponibilidad_inicio, 
        registro_disponibilidad_termino = registro_disponibilidad_termino, registro_contrataciones_inicio = registro_contrataciones_inicio, 
        registro_contrataciones_termino = registro_contrataciones_termino, registro_horarios_secretaria_inicio = registro_horarios_secretaria_inicio, 
        registro_horarios_secretaria_termino = registro_horarios_secretaria_termino, registro_aprobacion_coordi_docente_inicio = registro_aprobacion_coordi_docente_inicio, 
        registro_aprobacion_coordi_docente_termino = registro_aprobacion_coordi_docente_termino)
        session.add(ciclo_escolar)
        session.commit()
        return True
    except Exception as error:
        print(error)
        return False

#Consultar
def query_row_ciclo_escolar(id_ciclo_escolar: int):
    try:
        ciclo_escolar = session.query(CicloEscolar.id_ciclo_escolar, CicloEscolar.periodo, CicloEscolar.anio, CicloEscolar.registro_grupos_inicio,
        CicloEscolar.registro_grupos_termino, CicloEscolar.registro_disponibilidad_inicio, CicloEscolar.registro_disponibilidad_termino,
        CicloEscolar.registro_contrataciones_inicio, CicloEscolar.registro_contrataciones_termino, CicloEscolar.registro_horarios_secretaria_inicio,
        CicloEscolar.registro_horarios_secretaria_termino, CicloEscolar.registro_aprobacion_coordi_docente_inicio,
        CicloEscolar.registro_aprobacion_coordi_docente_termino).filter(
            CicloEscolar.id_ciclo_escolar == id_ciclo_escolar
        ).first()
        if ciclo_escolar:
                return dict(ciclo_escolar)
        else:
                return None
    except Exception as error:
        print(error)
        return None

#Actualizar
def update_row_ciclo_escolar(id_ciclo_escolar, periodo, anio, registro_grupos_inicio, registro_grupos_termino, registro_disponibilidad_inicio,
registro_disponibilidad_termino, registro_contrataciones_inicio, registro_contrataciones_termino, registro_horarios_secretaria_inicio,
registro_horarios_secretaria_termino, registro_aprobacion_coordi_docente_inicio, registro_aprobacion_coordi_docente_termino):
    try:
        session.query(CicloEscolar).filter(
                CicloEscolar.id_ciclo_escolar == id_ciclo_escolar 
        ).update(
                {
                    CicloEscolar.periodo : periodo,
                    CicloEscolar.anio : anio,
                    CicloEscolar.registro_grupos_inicio : registro_grupos_inicio,
                    CicloEscolar.registro_grupos_termino : registro_grupos_termino,
                    CicloEscolar.registro_disponibilidad_inicio : registro_disponibilidad_inicio,
                    CicloEscolar.registro_disponibilidad_termino : registro_disponibilidad_termino,
                    CicloEscolar.registro_contrataciones_inicio : registro_contrataciones_inicio,
                    CicloEscolar.registro_contrataciones_termino : registro_contrataciones_termino,
                    CicloEscolar.registro_horarios_secretaria_inicio : registro_horarios_secretaria_inicio,
                    CicloEscolar.registro_horarios_secretaria_termino : registro_horarios_secretaria_termino,
                    CicloEscolar.registro_aprobacion_coordi_docente_inicio : registro_aprobacion_coordi_docente_inicio,
                    CicloEscolar.registro_aprobacion_coordi_docente_termino : registro_aprobacion_coordi_docente_termino,
                }
        )
        session.commit()
        return True
    except Exception as error:
        print(error)
        return False

#Eliminar
def delete_row_ciclo_escolar(id_ciclo_escolar: int):
    try:
        session.query(CicloEscolar).filter(
                CicloEscolar.id_ciclo_escolar == id_ciclo_escolar
        ).delete()
        session.commit()
        return True
    except Exception as error:
        print(error)
        return False

'''print(insert_row_ciclo_escolar(periodo = '3', anio = 2022, registro_grupos_inicio = '02-10-2022', registro_grupos_termino = '09-10-2022', registro_disponibilidad_inicio = '10-10-2022',
registro_disponibilidad_termino = '16-10-2022', registro_contrataciones_inicio = '17-10-2022', registro_contrataciones_termino = '23-10-2022', registro_horarios_secretaria_inicio = '24-10-2022',
registro_horarios_secretaria_termino = '30-10-2022', registro_aprobacion_coordi_docente_inicio = '31-10-2022', registro_aprobacion_coordi_docente_termino = '06-11-2022'))'''


'''print(update_row_ciclo_escolar(id_ciclo_escolar= 2, periodo = '2', anio = 2021, registro_grupos_inicio = '25-09-2022', registro_grupos_termino = '02-10-2022', registro_disponibilidad_inicio = '10-10-2022',
registro_disponibilidad_termino = '16-10-2022', registro_contrataciones_inicio = '17-10-2022', registro_contrataciones_termino = '23-10-2022', registro_horarios_secretaria_inicio = '24-10-2022',
registro_horarios_secretaria_termino = '30-10-2022', registro_aprobacion_coordi_docente_inicio = '31-10-2022', registro_aprobacion_coordi_docente_termino = '06-11-2022'))'''
#print(query_row_ciclo_escolar(id_ciclo_escolar = 2))
#print(delete_row_ciclo_escolar(id_ciclo_escolar = 1))


######################################################## Carreras

def insert_row_carreras(nombre_carrera : str, coordinador_carrera : int):
        try:
            carrera = Carreras(nombre_carrera = nombre_carrera, coordinador_carrera = coordinador_carrera)
            session.add(carrera)
            session.commit()
            return True
        except Exception as error:
            print(error)
            return False

#Consultar
def query_row_carreras(id_carrera: int):
    try:
        carrera = session.query(Carreras.id_carrera, Carreras.nombre_carrera, Usuarios.id_usuario, Usuarios.nombre_usuario, Usuarios.apellido_paterno, Usuarios.apellido_materno).join(
           Usuarios, Carreras.id_carrera == id_carrera
        ).first()
        if carrera:
                return dict(carrera)
        else:
                return None
    except Exception as error:
        print(error)
        return None

#Actualizar
def update_row_carreras(id_carrera, nombre_carrera, coordinador_carrera):
    try:
        session.query(Carreras).filter(
                Carreras.id_carrera == id_carrera 
        ).update(
                {
                    Carreras.nombre_carrera : nombre_carrera,
                    Carreras.coordinador_carrera : coordinador_carrera
                }
        )
        session.commit()
        return True
    except Exception as error:
        print(error)
        return False

#Eliminar
def delete_row_carreras(id_carrera: int):
    try:
        session.query(Carreras).filter(
                Carreras.id_carrera == id_carrera
        ).delete()
        session.commit()
        return True
    except Exception as error:
        print(error)
        return False

#print(insert_row_carreras(nombre_carrera = "Ingeniería en Desarrollo y Gestión de Software", coordinador_carrera = 2))
'''print(update_row_carreras(id_carrera = 3, nombre_carrera = "Ingeniería en Desarrollo y Gestión de Software", coordinador_carrera = 2))
#print(delete_row_carreras(id_carrera = 2))
print(query_row_carreras(id_carrera = 3))'''


################################################# PLANES DE ESTUDIOS

# INSERTAR
def insert_row_plan_estudios(nombre_materia : str, cuatrimestre : int, total_horas: int, total_horas_semana: int, carrera: int):
        try:
            plan_estudios = PlanEstudios(nombre_materia = nombre_materia, cuatrimestre = cuatrimestre, total_horas = total_horas,
            total_horas_semana = total_horas_semana, carrera = carrera)
            session.add(plan_estudios)
            session.commit()
            return True
        except Exception as error:
            print(error)
            return False

#Consultar
def query_row_plan_estudios(carrera: int):
    try:
        plan_estudios = session.query(PlanEstudios.id_materia, PlanEstudios.nombre_materia, PlanEstudios.cuatrimestre, 
        PlanEstudios.total_horas, PlanEstudios.total_horas_semana, PlanEstudios.carrera, Carreras.nombre_carrera).join(
           Carreras, PlanEstudios.carrera == carrera
        )
        if plan_estudios:
                return [ dict(i) for i in plan_estudios ]
        else:
                return None
    except Exception as error:
        print(error)
        return None

#Actualizar
def update_row_plan_estudios(id_materia: int, nombre_materia : str, cuatrimestre : int, total_horas: int, total_horas_semana: int, carrera: int):
    try:
        session.query(PlanEstudios).filter(
                PlanEstudios.id_materia == id_materia 
        ).update(
                {
                    PlanEstudios.nombre_materia : nombre_materia,
                    PlanEstudios.cuatrimestre : cuatrimestre,
                    PlanEstudios.total_horas : total_horas,
                    PlanEstudios.total_horas_semana : total_horas_semana,
                    PlanEstudios.carrera : carrera
                }
        )
        session.commit()
        return True
    except Exception as error:
        print(error)
        return False

#Eliminar
def delete_row_plan_estudios(id_materia: int):
    try:
        session.query(PlanEstudios).filter(
                PlanEstudios.id_materia == id_materia
        ).delete()
        session.commit()
        return True
    except Exception as error:
        print(error)
        return False

'''print(insert_row_plan_estudios(nombre_materia = 'Programación I.', cuatrimestre = 1, total_horas = 200, total_horas_semana = 5, carrera = 3))
print(insert_row_plan_estudios(nombre_materia = 'Bases de Datos I.', cuatrimestre = 2, total_horas = 250, total_horas_semana = 6, carrera = 3))
print(insert_row_plan_estudios(nombre_materia = 'Desarrollo Web', cuatrimestre = 3, total_horas = 300, total_horas_semana = 7, carrera = 3))'''
#print(update_row_plan_estudios(id_materia = 3, nombre_materia = 'Desarrollo Móvil', cuatrimestre = 4, total_horas = 250, total_horas_semana = 6, carrera = 2))
#print(delete_row_plan_estudios(id_materia = 2))
#print(query_row_plan_estudios(carrera = 2))

'''print(delete_row_plan_estudios(id_materia = 1))
print(delete_row_plan_estudios(id_materia = 3))'''
#print(query_row_plan_estudios(carrera = 3))


######################################## TURNOS

def insert_row_turnos(nombre_turno : str, hora_entrada : str, hora_salida: str):
        try:
            turno = Turnos(nombre_turno = nombre_turno, hora_entrada = hora_entrada, hora_salida = hora_salida)
            session.add(turno)
            session.commit()
            return True
        except Exception as error:
            print(error)
            return False

#Consultar
def query_row_turnos(id_turno: int):
    try:
        turno = session.query(Turnos.id_turno, Turnos.nombre_turno, Turnos.hora_entrada, Turnos.hora_salida).filter(
           Turnos.id_turno == id_turno
        ).first()
        if turno:
                return dict(turno)
        else:
                return None
    except Exception as error:
        print(error)
        return None

#Actualizar
def update_row_turnos(id_turno: int, nombre_turno : str, hora_entrada : str, hora_salida: str):
    try:
        session.query(Turnos).filter(
                Turnos.id_turno == id_turno 
        ).update(
                {
                    Turnos.nombre_turno : nombre_turno,
                    Turnos.hora_entrada : hora_entrada,
                    Turnos.hora_salida : hora_salida
                }
        )
        session.commit()
        return True
    except Exception as error:
        print(error)
        return False

#Eliminar
def delete_row_turnos(id_turno: int):
    try:
        session.query(Turnos).filter(
                Turnos.id_turno == id_turno
        ).delete()
        session.commit()
        return True
    except Exception as error:
        print(error)
        return False

#print(insert_row_turnos(nombre_turno = "Matutino", hora_entrada = "07:00", hora_salida = "14:00"))
#print(insert_row_turnos(nombre_turno = "Vespertino", hora_entrada = "14:00", hora_salida = "21:00"))
print(update_row_turnos(id_turno = 4, nombre_turno = "Vespertino", hora_entrada = "14:00", hora_salida = "20:00"))
#print(delete_row_turnos(id_turno = 1))
'''print(insert_row_turnos(nombre_turno = "Matutino", hora_entrada = "07:00", hora_salida = "14:00"))
print(insert_row_turnos(nombre_turno = "Vespertino", hora_entrada = "14:00", hora_salida = "21:00"))'''
print(query_row_turnos(id_turno = 4))
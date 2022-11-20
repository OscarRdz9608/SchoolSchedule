from sqlalchemy import Column, Integer, String, SmallInteger, Date, ForeignKey, Time

from database import Base


class Usuarios(Base):
    __tablename__ = 'usuarios'

    id_usuario = Column(Integer(), primary_key = True)
    nombre_usuario = Column(String(20), nullable = False)
    apellido_paterno = Column(String(15), nullable = False)
    apellido_materno = Column(String(15), nullable = False)
    email = Column(String(60), nullable = False, unique = True)
    tipo_usuario = Column(String(5), nullable = False)

class Carreras(Base):
    __tablename__ = 'carreras'

    id_carrera = Column(Integer(), primary_key = True)
    nombre_carrera = Column(String(60), nullable = False)
    coordinador_carrera = Column(Integer(), ForeignKey("usuarios.id_usuario", ondelete="CASCADE"), nullable = False) ### FOREIGN KEY USUARIOS(ID)

class PlanEstudios(Base):
    __tablename__ = 'plan_estudios'

    id_materia = Column(Integer(), primary_key = True)
    nombre_materia = Column(String(60), nullable = False)
    cuatrimestre = Column(SmallInteger(), nullable = False)
    total_horas = Column(SmallInteger(), nullable = False)
    total_horas_semana = Column(SmallInteger(), nullable = False)
    carrera = Column(SmallInteger(), ForeignKey("carreras.id_carrera", ondelete="CASCADE"), nullable = False) ### FOREIGN KEY CARRERAS(ID)

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

class Grupo(Base):
    __tablename__ = 'grupos'
    id_grupo = Column(Integer(), primary_key = True)
    cuatrimestre = Column(Integer(), nullable = False)
    no_grupo = Column(SmallInteger(), nullable = False)
    hora_entrada_minima = Column(Time(), nullable = False)
    hora_salida_maxima = Column(Time(), nullable = False)
    ciclo_escolar = Column(Integer(), ForeignKey("ciclo_escolar.id_ciclo_escolar", ondelete="CASCADE"), nullable = False) # FOREIGN KEY CiCLOESCOLAR(ID)
    carrera = Column(SmallInteger(), ForeignKey("carreras.id_carrera", ondelete="CASCADE"), nullable = False) ### FOREIGN KEY CARRERAS(ID)



####################################################### Tipo Docente #######################################################

class TipoDocente(Base):
    __tablename__='tipodocente'
    id_tipo_docente= Column(Integer(), primary_key = True)
    tipo_docente = Column(String(60), nullable=False)


####################################### AREA PRINCIPAL #############################################

class arePrincipal(Base):
    __tablename__='areaprincipal'
    id_area_principal= Column(Integer(), primary_key = True)
    area_principal = Column(String(60), nullable=False)


#################################################### DOCENTES  ########################################

class RegistroDocente(Base):
    __tablename__ ='docentes'
    id_registro_docente = Column(Integer(), primary_key = True)
    nombre_docente = Column(String(60), nullable = False)
    apellido_paterno = Column(String(15), nullable = False)
    apellido_materno = Column(String(15), nullable = False)
    email = Column(String(60), nullable = False, unique = True)
    tipo_maestro = Column(Integer(), nullable = False)
    area_principal = Column(Integer(), nullable = False)
   # tipo_maestro = Column(Integer(), ForeignKey("tipodocente.id_tipo_docente", ondelete="CASCADE"), nullable = False)
   # area_principal = Column(Integer(), ForeignKey("areaprincipal.id_area_principal", ondelete="CASCADE"), nullable = False) 


########################################################## DISPONIBILIDAD ########################################################

class Registrodisponibilidad(Base):
    __tablename__='registrodisponibilidad'
    id_disponibilidad = Column(Integer(), primary_key = True)
    id_docente = Column(Integer(), nullable = False)
    id_ciclo_escolar = Column(Integer(), nullable = False)
    lunesEntrada = Column(Time(), nullable = False)
    lunesSalida = Column(Time(), nullable = False)
    martesEntrada = Column(Time(), nullable = False)
    martesSalida = Column(Time(), nullable = False)
    miercolesEntrada = Column(Time(), nullable = False)
    miercolesSalida = Column(Time(), nullable = False)
    juevesEntrada = Column(Time(), nullable = False)
    juevesSalida = Column(Time(), nullable = False)
    viernesEntrada = Column(Time(), nullable = False)
    viernesSalida = Column(Time(), nullable = False)
    sabadoEntrada = Column(Time(), nullable = False)
    sabadoSalida = Column(Time(), nullable = False)

   
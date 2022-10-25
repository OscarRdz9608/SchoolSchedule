"""coding=utf-8."""
 
from sqlalchemy.orm import Session 
from . import models, schemas

#################USUARIO###################
#Insertar
def insert_row_Usuarios(db: Session, user_base: schemas.UserBase):
        try:
            db_user = models.Usuarios(nombre_usuario = user_base.nombre_usuario, apellido_paterno = user_base.apellido_paterno,
                apellido_materno = user_base.apellido_materno, email = user_base.email, tipo_usuario = user_base.tipo_usuario)
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return True
        except Exception as error:
            print(error)
            return False
#Consultar por email
def query_row_Usuarios(db: Session, email: str):
    try:
        user = db.query(models.Usuarios.id_usuario, models.Usuarios.nombre_usuario, models.Usuarios.apellido_paterno, 
        models.Usuarios.apellido_materno, models.Usuarios.email, models.Usuarios.tipo_usuario).filter(
            models.Usuarios.email == email
        ).first()
        if user:
                return dict(user)
        else:
                return None
    except Exception as error:
        print(error)
        return None
#Actualizar
def update_row_Usuarios(db: Session, user_base: schemas.UserBase):
    try:
        db.query(models.Usuarios).filter(
                models.Usuarios.id_usuario == user_base.id_usuario 
        ).update(
                {
                    models.Usuarios.nombre_usuario : user_base.nombre_usuario,
                    models.Usuarios.apellido_paterno : user_base.apellido_paterno,
                    models.Usuarios.apellido_materno : user_base.apellido_materno,
                    models.Usuarios.email : user_base.email,
                    models.Usuarios.tipo_usuario : user_base.tipo_usuario,
                }
        )
        db.commit()
        return True
    except Exception as error:
        print(error)
        return False
#Eliminar
def delete_row_Usuarios(db: Session, email: str):
    try:
        db.query(models.Usuarios).filter(
                models.Usuarios.email == email
        ).delete()
        db.commit()
        return True
    except Exception as error:
        print(error)
        return False

#################CICLO ESCOLAR###################
#Insertar
def insert_row_ciclo_escolar(db: Session, cicloUser: schemas.CicloEscolarBase):
    try:
        ciclo_escolar = models.CicloEscolar( 
        periodo= cicloUser.periodo,
        anio = cicloUser.anio,
        registro_grupos_inicio = cicloUser.registro_grupos_inicio,
        registro_grupos_termino = cicloUser.registro_grupos_termino, 
        registro_disponibilidad_inicio = cicloUser.registro_disponibilidad_inicio,
        registro_disponibilidad_termino = cicloUser.registro_disponibilidad_termino,
        registro_contrataciones_inicio =  cicloUser.registro_contrataciones_inicio,
        registro_contrataciones_termino = cicloUser.registro_contrataciones_termino,
        registro_horarios_secretaria_inicio = cicloUser.registro_horarios_secretaria_inicio,
        registro_horarios_secretaria_termino = cicloUser.registro_horarios_secretaria_termino,
        registro_aprobacion_coordi_docente_inicio = cicloUser.registro_aprobacion_coordi_docente_inicio,
        registro_aprobacion_coordi_docente_termino = cicloUser.registro_aprobacion_coordi_docente_termino)       
        db.add(ciclo_escolar)
        db.commit()
        db.refresh(ciclo_escolar)
        return True
    except Exception as error:
        print(error)
        return False

#Actualizar
def update_row_ciclo_escolar(db: Session, ciclo_escolar: schemas.CicloEscolarBase):
    try:
        db.query(models.CicloEscolar).filter(
                models.CicloEscolar.id_ciclo_escolar == ciclo_escolar.id_ciclo_escolar 
        ).update(
                {
                    models.CicloEscolar.periodo : ciclo_escolar.periodo,
                    models.CicloEscolar.anio : ciclo_escolar.anio,
                    models.CicloEscolar.registro_grupos_inicio : ciclo_escolar.registro_grupos_inicio,
                    models.CicloEscolar.registro_grupos_termino : ciclo_escolar.registro_grupos_termino,
                    models.CicloEscolar.registro_disponibilidad_inicio : ciclo_escolar.registro_disponibilidad_inicio,
                    models.CicloEscolar.registro_disponibilidad_termino : ciclo_escolar.registro_disponibilidad_termino,
                    models.CicloEscolar.registro_contrataciones_inicio : ciclo_escolar.registro_contrataciones_inicio,
                    models.CicloEscolar.registro_contrataciones_termino : ciclo_escolar.registro_contrataciones_termino,
                    models.CicloEscolar.registro_horarios_secretaria_inicio : ciclo_escolar.registro_horarios_secretaria_inicio,
                    models.CicloEscolar.registro_horarios_secretaria_termino : ciclo_escolar.registro_horarios_secretaria_termino,
                    models.CicloEscolar.registro_aprobacion_coordi_docente_inicio : ciclo_escolar.registro_aprobacion_coordi_docente_inicio,
                    models.CicloEscolar.registro_aprobacion_coordi_docente_termino : ciclo_escolar.registro_aprobacion_coordi_docente_termino,
                }
        )
        db.commit()
        return True
    except Exception as error:
        print(error)
        return False

#Eliminar
def delete_row_ciclo_escolar(db: Session, id_ciclo_escolar: int):
    try:
        db.query(models.CicloEscolar).filter(
                models.CicloEscolar.id_ciclo_escolar == id_ciclo_escolar
        ).delete()
        db.commit()
        return True
    except Exception as error:
        print(error)
        return False

####################CARRERA######################
def insert_row_carreras(db:Session,nombre_carrera : str, coordinador_carrera : int):
        try:
            carrera = models.Carreras(nombre_carrera = nombre_carrera, coordinador_carrera = coordinador_carrera)
            db.add(carrera)
            db.commit()
            return True
        except Exception as error:
            print(error)
            return False

#Consultar
def query_row_carreras(db: Session, id_carrera: int):
    try:
        carrera = db.query(models.Carreras.id_carrera, models.Carreras.nombre_carrera, models.Usuarios.id_usuario, models.Usuarios.nombre_usuario, models.Usuarios.apellido_paterno, models.Usuarios.apellido_materno).join(
           models.Usuarios, models.Carreras.id_carrera == id_carrera
        ).first()
        if carrera:
                return dict(carrera)
        else:
                return None
    except Exception as error:
        print(error)
        return None

#Actualizar
def update_row_carreras(db:Session, id_carrera, nombre_carrera, coordinador_carrera):
    try:
        db.query(models.Carreras).filter(
                models.Carreras.id_carrera == id_carrera 
        ).update(
                {
                    models.Carreras.nombre_carrera : nombre_carrera,
                    models.Carreras.coordinador_carrera : coordinador_carrera
                }
        )
        db.commit()
        return True
    except Exception as error:
        print(error)
        return False

#Eliminar
def delete_row_carreras(db:Session, id_carrera: int):
    try:
        db.query(models.Carreras).filter(
                models.Carreras.id_carrera == id_carrera
        ).delete()
        db.commit()
        return True
    except Exception as error:
        print(error)
        return False

################################################# PLANES DE ESTUDIOS

# INSERTAR
def insert_row_plan_estudios(db:Session,nombre_materia : str, cuatrimestre : int, total_horas: int, total_horas_semana: int, carrera: int):
        try:
            plan_estudios = models.PlanEstudios(nombre_materia = nombre_materia, cuatrimestre = cuatrimestre, total_horas = total_horas,
            total_horas_semana = total_horas_semana, carrera = carrera)
            db.add(plan_estudios)
            db.commit()
            return True
        except Exception as error:
            print(error)
            return False

#Consultar
def query_row_plan_estudios(db:Session,carrera: int):
    try:
        plan_estudios = db.query(models.PlanEstudios.id_materia, models.PlanEstudios.nombre_materia, models.PlanEstudios.cuatrimestre, 
        models.PlanEstudios.total_horas, models.PlanEstudios.total_horas_semana, models.PlanEstudios.carrera, models.Carreras.nombre_carrera).join(
           models.Carreras, models.PlanEstudios.carrera == carrera
        )
        if plan_estudios:
                return [ dict(i) for i in plan_estudios ]
        else:
                return None
    except Exception as error:
        print(error)
        return None

#Actualizar
def update_row_plan_estudios(db:Session, plan_estudioBase: schemas.PlanEstudiosBase):
    try:
        db.query(schemas.PlanEstudiosBase).filter(
                schemas.PlanEstudiosBase.id_materia == plan_estudioBase.id_materia 
        ).update(
                {
                    schemas.PlanEstudios.nombre_materia : plan_estudioBase.nombre_materia,
                    schemas.PlanEstudios.cuatrimestre : plan_estudioBase.cuatrimestre,
                    schemas.PlanEstudios.total_horas : plan_estudioBase.total_horas,
                    schemas.PlanEstudios.total_horas_semana : plan_estudioBase.total_horas_semana,
                    schemas.PlanEstudios.carrera : plan_estudioBase.carrera
                }
        )
        db.commit()
        return True
    except Exception as error:
        print(error)
        return False

#Eliminar
def delete_row_plan_estudios(db: Session,id_materia: int):
    try:
        db.query(schemas.PlanEstudiosBase).filter(
                schemas.PlanEstudiosBase.id_materia == id_materia
        ).delete()
        db.commit()
        return True
    except Exception as error:
        print(error)
        return False

######################################## TURNOS

def insert_row_turnos(db:Session,nombre_turno : str, hora_entrada : str, hora_salida: str):
        try:
            turno = models.Turnos(nombre_turno = nombre_turno, hora_entrada = hora_entrada, hora_salida = hora_salida)
            db.add(turno)
            db.commit()
            return True
        except Exception as error:
            print(error)
            return False

#Consultar
def query_row_turnos(db:Session,id_turno: int):
    try:
        turno = db.query(models.Turnos.id_turno, models.Turnos.nombre_turno, models.Turnos.hora_entrada, models.Turnos.hora_salida).filter(
           models.Turnos.id_turno == id_turno
        ).first()
        if turno:
                return dict(turno)
        else:
                return None
    except Exception as error:
        print(error)
        return None

#Actualizar
def update_row_turnos(db:Session, id_turno: int, nombre_turno : str, hora_entrada : str, hora_salida: str):
    try:
        db.query(models.Turnos).filter(
                models.Turnos.id_turno == id_turno 
        ).update(
                {
                    models.Turnos.nombre_turno : nombre_turno,
                    models.Turnos.hora_entrada : hora_entrada,
                    models.Turnos.hora_salida : hora_salida
                }
        )
        db.commit()
        return True
    except Exception as error:
        print(error)
        return False

#Eliminar
def delete_row_turnos(db:Session,id_turno: int):
    try:
        db.query(models.Turnos).filter(
                models.Turnos.id_turno == id_turno
        ).delete()
        db.commit()
        return True
    except Exception as error:
        print(error)
        return False
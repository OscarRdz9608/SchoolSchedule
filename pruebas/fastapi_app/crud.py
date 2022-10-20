"""coding=utf-8."""
 
from sqlalchemy.orm import Session 
from . import models, schemas

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


def query_row_ciclo_escolar(db: Session, id_ciclo_escolar: int):
    try:
        ciclo_escolar = db.query(models.CicloEscolar.id_ciclo_escolar, models.CicloEscolar.periodo, models.CicloEscolar.anio, models.CicloEscolar.registro_grupos_inicio,
        models.CicloEscolar.registro_grupos_termino, models.CicloEscolar.registro_disponibilidad_inicio, models.CicloEscolar.registro_disponibilidad_termino,
        models.CicloEscolar.registro_contrataciones_inicio, models.CicloEscolar.registro_contrataciones_termino, models.CicloEscolar.registro_horarios_secretaria_inicio,
        models.CicloEscolar.registro_horarios_secretaria_termino, models.CicloEscolar.registro_aprobacion_coordi_docente_inicio,
        models.CicloEscolar.registro_aprobacion_coordi_docente_termino).filter(
            models.CicloEscolar.id_ciclo_escolar == id_ciclo_escolar
        ).first()
        if ciclo_escolar:
                return dict(ciclo_escolar)
        else:
                return None
    except Exception as error:
        print(error)
        return None
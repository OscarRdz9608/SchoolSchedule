"""coding=utf-8."""
 
from typing import List
 
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import crud, models, schemas
from  database import SessionLocal, engine
 
models.Base.metadata.create_all(bind=engine)
 
app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
      
 ########################################## DIRECCIONAR ######################################################
@app.get("/")
async def read_root():
    return  RedirectResponse(url="/docs")

############################################ USUARIOS #################################################

#INSERTAR
@app.post("/usuarios/", tags = ["usuarios"], status_code=status.HTTP_202_ACCEPTED)
async def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    if crud.insert_row_Usuarios(db=db, user_base=user) is True:
        return {"message": "Usuario agregado correctamente"}
    else:
        raise HTTPException(status_code=400, detail="Correo ya registrado")

#CONSULTAR 1 REGISTRO
@app.get("/usuarios/{email}", tags = ["usuarios"], status_code=status.HTTP_202_ACCEPTED,
response_model=schemas.UserBase)
async def read_user(email: str, db: Session = Depends(get_db)):
    db_user = crud.query_row_Usuarios(db=db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user

#CONSULTAR N REGISTROS
@app.get("/usuarios/", tags=["usuarios"], response_model= List[schemas.UserBase], 
status_code=status.HTTP_202_ACCEPTED)
async def read_user(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_user = crud.query_rows_usuarios(db= db, limit=limit, offset=offset)
    if db_user is not None:
        return db_user
    else:
        raise HTTPException(status_code= 404, detail="Consulta no valida")

#ACTUALIZAR
@app.put("/usuarios/", tags=["usuarios"], status_code=status.HTTP_202_ACCEPTED)
async def update_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    if crud.update_row_Usuarios(db=db, user_base=user) is True:
        return {"message": "Usuario actualizado"}
    else:
        raise HTTPException(status_code=404, detail="No se actualizó correctamente")

#BORRAR
@app.delete("/usuarios/{email}", tags=["usuarios"], status_code=status.HTTP_202_ACCEPTED)
async def delete_user(email: str, db: Session = Depends(get_db)):
    if crud.delete_row_Usuarios(db=db, email=email) is True:
        return {"message": "Usuario eliminado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="No se eliminó correctamente")


############################################ CARRERAS #################################################

#INSERTAR
@app.post("/carreras/", tags = ["carreras"], status_code=status.HTTP_202_ACCEPTED)
async def create_carrera(carrera: schemas.CarrerasBase, db: Session = Depends(get_db)):
    if crud.insert_row_carreras(db=db, user_carrera= carrera) is True:
        return {"message": "Carrera agregada correctamente"}
    else:
        raise HTTPException(status_code=400, detail="No se agregó correctamente")

#CONSULTAR 1 REGISTRO
@app.get("/carreras/{id_carrera}", tags = ["carreras"], status_code=status.HTTP_202_ACCEPTED, 
response_model=schemas.CarrerasResponseBase)
async def read_carrera(id_carrera: int, db: Session = Depends(get_db)):
    db_carreras = crud.query_row_carreras(db= db, id_carrera= id_carrera)
    if db_carreras is None:
        raise HTTPException(status_code=404, detail="Carrera no encontrada")
    return db_carreras

#ACTUALIZAR
@app.put("/carreras/", tags=["carreras"], status_code=status.HTTP_202_ACCEPTED)
async def update_carrera(carrera: schemas.CarrerasBase, db: Session = Depends(get_db)):
    if crud.update_row_carreras(db=db, carrera=carrera) is True:
        return {"message": "Carrera actualizada correctamente"}
    else:
        raise HTTPException(status_code=404, detail="No se actualizó correctamente")

#BORRAR
@app.delete("/carreras/{id_carrera}", tags=["carreras"], status_code=status.HTTP_202_ACCEPTED)
async def delete_carrera(id_carrera: int, db: Session = Depends(get_db)):
    if crud.delete_row_carreras(db=db, id_carrera=id_carrera) is True:
        return {"message": "Carrera eliminada correctamente"}
    else:
        raise HTTPException(status_code=404, detail="No se eliminó correctamente")

########################################################### CICLO ESCOLAR ############################

#INSERTAR
@app.post("/ciclo_escolar/", tags = ["ciclo escolar"], status_code=status.HTTP_202_ACCEPTED)
async def create_ciclo_escolar(ciclo_escolar: schemas.CicloEscolarBase, db: Session = Depends(get_db)):
    if crud.insert_row_ciclo_escolar(db=db, cicloUser= ciclo_escolar) is True:
        return { "message" : "Ciclo escolar agregado" }        
    else:
        raise HTTPException(status_code=400, detail="No se agrego correctamente")

@app.get("/ciclo_escolar/{id_ciclo_escolar}", tags = ["ciclo escolar"], status_code=status.HTTP_202_ACCEPTED,
response_model=schemas.CicloEscolarBase)
async def read_ciclo_escolar(id_ciclo_escolar: int, db: Session = Depends(get_db)):
    db_ciclo_escolar = crud.query_row_ciclo_escolar(db=db, id_ciclo_escolar= id_ciclo_escolar)
    if db_ciclo_escolar is None:
        raise HTTPException(status_code=404, detail="Ciclo escolar no encontrado")
    else:
        return db_ciclo_escolar

#ACTUALIZAR
@app.put("/ciclo_escolar/", tags=["ciclo escolar"], status_code=status.HTTP_202_ACCEPTED)
async def update_ciclo_escolar(user: schemas.CicloEscolarBase, db: Session = Depends(get_db)):
    if crud.update_row_ciclo_escolar(db=db, ciclo_escolar=user) is True:
        return {"message": "Ciclo escolar actualizado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="No se actualizó correctamente")

#BORRAR
@app.delete("/ciclo_escolar/{id_ciclo_escolar}", tags=["ciclo escolar"], status_code=status.HTTP_202_ACCEPTED)
async def delete_user(id_ciclo_escolar: int, db: Session = Depends(get_db)):
    if crud.delete_row_ciclo_escolar(db=db, id_ciclo_escolar= id_ciclo_escolar) is True:
        return {"message": "Ciclo escolar eliminado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="No se eliminó correctamente")

########################################################### PLAN DE ESTUDIOS ############################

@app.post("/plan_estudios/", tags = ["plan estudios"], status_code=status.HTTP_202_ACCEPTED)
async def create_plan_estudios(plan_estudios: List[schemas.PlanEstudiosBase], db: Session = Depends(get_db)):
    contador = 0
    for i in plan_estudios:
        if crud.insert_row_plan_estudios(db=db, user_plan=i) is True:
            contador+=1
        else:
            raise HTTPException(status_code=400, detail="No se agrego correctamente")
    if contador == len(plan_estudios):
        contador = 0
        return {"message": "Plan de estudios agregado"}
    else:
        raise HTTPException(status_code=400, detail="No se agrego correctamente")

@app.get("/plan_estudios/{id_plan_estudios}", tags = ["plan estudios"], status_code=status.HTTP_202_ACCEPTED,
response_model=schemas.PlanEstudiosBase)
async def read_plan_estudios(id_plan_estudios: int, db: Session = Depends(get_db)):
    db_plan_estudios = crud.query_row_plan_estudios(db=db, id_plan_estudios= id_plan_estudios)
    if db_plan_estudios is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    else:
        return db_plan_estudios

@app.get("/plan_estudios/", tags = ["plan estudios"], status_code=status.HTTP_202_ACCEPTED,
response_model=List[schemas.PlanEstudiosBase])
async def read_plan_estudios_completo(carrera: int, db: Session = Depends(get_db)):
    db_plan_estudios = crud.query_rows_plan_estudios(db=db, carrera= carrera)
    if db_plan_estudios is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    else:
        return db_plan_estudios

#ACTUALIZAR
@app.put("/plan_estudios/", tags=["plan estudios"], status_code=status.HTTP_202_ACCEPTED)
async def update_plan_estudios(plan_estudios: List[schemas.PlanEstudiosBase], db: Session = Depends(get_db)):
    contador = 0
    for i in plan_estudios:
        if crud.update_row_plan_estudios(db=db, id_plan_estudios= i) is True:
            contador+=1
        else:
            raise HTTPException(status_code=400, detail="No se agrego correctamente")
    if contador == len(plan_estudios):
        contador = 0
        return {"message": "Plan de estudios actualizado correctamente"}
    else:
        raise HTTPException(status_code=400, detail="No se agrego correctamente")

#BORRAR
@app.delete("/plan_estudios/{id_plan_estudios}", tags=["plan estudios"], status_code=status.HTTP_202_ACCEPTED)
async def delete_plan_estudios(id_plan_estudios: int, db: Session = Depends(get_db)):
    if crud.delete_row_plan_estudios(db=db, id_plan_estudios= id_plan_estudios) is True:
        return {"message": "Materia eliminada correctamente"}
    else:
        raise HTTPException(status_code=404, detail="No se eliminó correctamente")

########################################################### GRUPOS ###################################

#INSERTAR
@app.post("/grupos/", tags = ["grupos"], status_code=status.HTTP_202_ACCEPTED)
async def create_grupo(grupo: schemas.GruposBase, db: Session = Depends(get_db)):
    if crud.insert_row_grupos(db=db, grupo_base= grupo) is True:
        return { "message" : "Grupo agregado correctamente" }        
    else:
        raise HTTPException(status_code=400, detail="No se agrego correctamente")

@app.get("/grupos/", tags = ["grupos"], status_code=status.HTTP_202_ACCEPTED,
response_model= List[schemas.GruposBase])
async def read_grupos(ciclo_escolar: int, carrera: int, db: Session = Depends(get_db)):
    db_grupos = crud.query_rows_grupos(db=db, ciclo_escolar= ciclo_escolar, carrera= carrera)
    if db_grupos is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    else:
        return db_grupos

#ACTUALIZAR
@app.put("/grupos/", tags=["grupos"], status_code=status.HTTP_202_ACCEPTED)
async def update_grupos(grupo: schemas.GruposBase, db: Session = Depends(get_db)):
    if crud.update_row_grupos(db=db, grupo_base= grupo) is True:
        return {"message": "Grupo actualizado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="No se actualizó correctamente")

#BORRAR
@app.delete("/grupos/{id_grupo}", tags=["grupos"], status_code=status.HTTP_202_ACCEPTED)
async def delete_user(id_grupo: int, db: Session = Depends(get_db)):
    if crud.delete_row_grupos(db=db, id_grupo= id_grupo) is True:
        return {"message": "Grupo eliminado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="No se eliminó correctamente")



#################################################### DOCENTES  ########################################

#INSERTAR
@app.post("/docentes/", tags = ["docentes"], status_code=status.HTTP_202_ACCEPTED)
async def insert_docente(docente:schemas.RegistroDocentesBase, db: Session = Depends(get_db)):
    if crud.insert_row_docente(db=db, docente_base=docente) is True:
        return { "message" : "Grupo agregado correctamente" }        
    else:
        raise HTTPException(status_code=400, detail="No se agrego correctamente")

###SELECT by ID
@app.get("/docentes/{id_tipo_docente}", tags = ["docentes"], status_code=status.HTTP_202_ACCEPTED,
response_model= List[schemas.RegistroDocentesBase])
async def read_docentes(id_tipo_docente: int, db: Session = Depends(get_db)):
    db_docentes = crud.query_rows_docente(db=db, id_tipo_docente= id_tipo_docente)
    if db_docentes is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    else:
        return db_docentes

###SELECT
@app.get("/docentes/", tags = ["docentes"], status_code=status.HTTP_202_ACCEPTED,  
response_model= List[schemas.RegistroDocentesBase])
async def read_docentes(db: Session = Depends(get_db)):
    db_docentes = crud.query_rows_docentes(db=db)
    if db_docentes is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    else:
        return db_docentes

###UPDATE
@app.put("/docentes/", tags=["docentes"], status_code=status.HTTP_202_ACCEPTED)
async def update_docentes(docente: schemas.RegistroDocentesBase, db: Session = Depends(get_db)):
    if crud.update_row_docente(db=db, docente_base= docente) is True:
        return {"message": "Docente actualizado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="No se actualizó correctamente")

###DELETE
@app.delete("/docentes/{id_docente}", tags=["docentes"], status_code=status.HTTP_202_ACCEPTED)
async def delete_docente(id_docente: int, db: Session = Depends(get_db)):
    if crud.delete_row_docente(db=db, id_docente= id_docente) is True:
        return {"message": "Docente eliminado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="No se eliminó correctamente")

#################################################### TIPO DOCENTES  ########################################
###INSERTAR
@app.post("/tipo_docentes/", tags = ["tipo docentes"], status_code=status.HTTP_202_ACCEPTED)
async def insert_tipo_docente(tipo_docente:schemas.TipoDocenteBase, db: Session = Depends(get_db)):
    if crud.insert_row_docente_registro(db=db, tipo_docente_base=tipo_docente) is True:
        return { "message" : "Tipo docente agregado correctamente" }        
    else:
        raise HTTPException(status_code=400, detail="No se agrego correctamente")

###SELECT
@app.get("/tipo_docentes/", tags = ["tipo docentes"], status_code=status.HTTP_202_ACCEPTED,
response_model= List[schemas.TipoDocenteBase])
async def read_tipo_docentes(db: Session = Depends(get_db)):
    db_tipo_docentes = crud.query_rows_tipo_docente(db=db)
    if db_tipo_docentes is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    else:
        return db_tipo_docentes

###SELECT BY ID
@app.get("/tipo_docentes/{id_tipo_docente}", tags = ["tipo docentes"], status_code=status.HTTP_202_ACCEPTED,
response_model= schemas.TipoDocenteBase)
async def read_tipo_docentes(id_tipo_docente: int, db: Session = Depends(get_db)):
    db_tipo_docentes = crud.query_row_tipo_docente(db=db, id_tipo_docente= id_tipo_docente)
    if db_tipo_docentes is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    else:
        return db_tipo_docentes
    
###UPDATE
@app.put("/tipo_docentes/", tags=["tipo docentes"], status_code=status.HTTP_202_ACCEPTED)
async def update_tipo_docentes(tipo_docente: schemas.TipoDocenteBase, db: Session = Depends(get_db)):
    if crud.update_row_tipo_docente(db=db, tipo_docente_base= tipo_docente) is True:
        return {"message": "Tipo docente actualizado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="No se actualizó correctamente")

###DELETE
@app.delete("/tipo_docentes/{id_tipo_docente}", tags=["tipo docentes"], status_code=status.HTTP_202_ACCEPTED)
async def delete_tipo_docente(id_tipo_docente: int, db: Session = Depends(get_db)):
    if crud.delete_row_tipo_docente(db=db, id_tipo_docente= id_tipo_docente) is True:
        return {"message": "Tipo docente eliminado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="No se eliminó correctamente")



#################################################### AREA PRINCIPAL  ########################################
###INSERTAR
@app.post("/area_principal/", tags = ["area principal"], status_code=status.HTTP_202_ACCEPTED)
async def insert_area_principal(area_principal:schemas.AreaPrincipalBase, db: Session = Depends(get_db)):
    if crud.insert_row_area_principal(db=db, area_principal_base=area_principal) is True:
        return { "message" : "Area principal agregado correctamente" }        
    else:
        raise HTTPException(status_code=400, detail="No se agrego correctamente")


###SELECT
@app.get("/area_principal/", tags = ["area principal"], status_code=status.HTTP_202_ACCEPTED,
response_model= List[schemas.AreaPrincipalBase])
async def read_area_principal(db: Session = Depends(get_db)):
    db_area_principal = crud.query_rows_area_principal(db=db)
    if db_area_principal is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    else:
        return db_area_principal

###SELECT BY ID
@app.get("/area_principal/{id_area_principal}", tags = ["area principal"], status_code=status.HTTP_202_ACCEPTED,
response_model= schemas.AreaPrincipalBase)
async def read_area_principal(id_area_principal: int, db: Session = Depends(get_db)):
    db_area_principal = crud.query_row_area_principal(db=db, id_area_principal= id_area_principal)
    if db_area_principal is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    else:
        return db_area_principal

###UPDATE
@app.put("/area_principal/{id_area_principal}", tags=["area principal"], status_code=status.HTTP_202_ACCEPTED)
async def update_area_principal(area_principal: schemas.AreaPrincipalBase, db: Session = Depends(get_db)):
    if crud.update_row_area_principal(db=db, area_principal_base= area_principal) is True:
        return {"message": "Area principal actualizado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="No se actualizó correctamente")

###DELETE
@app.delete("/area_principal/{id_area_principal}", tags=["area principal"], status_code=status.HTTP_202_ACCEPTED)
async def delete_area_principal(id_area_principal: int, db: Session = Depends(get_db)):
    if crud.delete_row_area_principal(db=db, id_area_principal= id_area_principal) is True:
        return {"message": "Area principal eliminado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="No se eliminó correctamente")


######################################### REGISTRO DE DISPONIBILIDAD  ########################################

###INSERTAR
@app.post("/registro_disponibilidad/", tags = ["registro disponibilidad"], status_code=status.HTTP_202_ACCEPTED)
async def insert_registro_disponibilidad(registro_disponibilidad:schemas.DisponibilidadBase, db: Session = Depends(get_db)):
    if crud.insert_row_disponibilidad(db=db, disponibilidad_base=registro_disponibilidad) is True:
        return { "message" : "Registro disponibilidad agregado correctamente" }        
    else:
        raise HTTPException(status_code=400, detail="No se agrego correctamente")

###SELECT
@app.get("/registro_disponibilidad/", tags = ["registro disponibilidad"], status_code=status.HTTP_202_ACCEPTED,
response_model= List[schemas.DisponibilidadBase])
async def read_registro_disponibilidad(db: Session = Depends(get_db)):
    db_registro_disponibilidad = crud.query_rows_disponibilidad(db=db)
    if db_registro_disponibilidad is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    else:
        return db_registro_disponibilidad
        
###SELECT BY ID
@app.get("/registro_disponibilidad/{id_registro_disponibilidad}", tags = ["registro disponibilidad"], status_code=status.HTTP_202_ACCEPTED,
response_model= schemas.DisponibilidadBase)
async def read_registro_disponibilidad(id_registro_disponibilidad: int, db: Session = Depends(get_db)):
    db_registro_disponibilidad = crud.query_row_disponibilidad_by_id(db=db, id_registro_disponibilidad= id_registro_disponibilidad)
    if db_registro_disponibilidad is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    else:
        return db_registro_disponibilidad

###UPDATE
@app.put("/registro_disponibilidad/{id_registro_disponibilidad}", tags=["registro disponibilidad"], status_code=status.HTTP_202_ACCEPTED)
async def update_registro_disponibilidad(registro_disponibilidad: schemas.DisponibilidadBase, db: Session = Depends(get_db)):
    if crud.update_row_disponibilidad(db=db, registro_disponibilidad_base= registro_disponibilidad) is True:
        return {"message": "Registro disponibilidad actualizado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="No se actualizó correctamente")
        
###DELETE
@app.delete("/registro_disponibilidad/{id_registro_disponibilidad}", tags=["registro disponibilidad"], status_code=status.HTTP_202_ACCEPTED)
async def delete_registro_disponibilidad(id_registro_disponibilidad: int, db: Session = Depends(get_db)):
    if crud.delete_row_disponibilidad(db=db, id_registro_disponibilidad= id_registro_disponibilidad) is True:
        return {"message": "Registro disponibilidad eliminado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="No se eliminó correctamente")

"""coding=utf-8."""
 
from this import d
from typing import List
 
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
 
from . import crud, models, schemas
from .database import SessionLocal, engine
 
models.Base.metadata.create_all(bind=engine)
 
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/usuarios/{email}", tags = ["usuarios"], status_code=status.HTTP_202_ACCEPTED)
async def read_user(email: str, db: Session = Depends(get_db)):
    db_user = crud.query_row_Usuarios(db=db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user

@app.post("/usuarios/", tags = ["usuarios"], status_code=status.HTTP_202_ACCEPTED)
async def create_user(user: schemas.WOIUserBase, db: Session = Depends(get_db)):
    if crud.insert_row_Usuarios(db=db, user_base=user) is True:
        return {"message": "Usuario agregado"}
    else:
        raise HTTPException(status_code=400, detail="Correo ya registrado")

@app.put("/usuarios/", tags=["usuarios"], status_code=status.HTTP_202_ACCEPTED)
async def update_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    if(crud.update_row_Usuarios(db=db, user_base=user)) is True:
        return {"message": "Usuario actualizado"}
    else:
        raise HTTPException(status_code=400, detail="No se actualizo correctamente")

@app.delete("/usuarios/{email}", tags=["usuarios"], status_code=status.HTTP_202_ACCEPTED)
async def delete_user(email: str, db: Session = Depends(get_db)):
    if crud.delete_row_Usuarios(db=db, email=email) is True:
        return {"message": "Usuario eliminado"}
    else:
        raise HTTPException(status_code=400, detail="No se elimino correctamente")

"""
@app.get("/ciclo_escolar/{id_ciclo_escolar}", tags = ["ciclo_escolar"], status_code=status.HTTP_202_ACCEPTED,
response_model=schemas.CicloEscolarBase)
async def read_ciclo_escolar(id_ciclo_escolar: int, db: Session = Depends(get_db)):
    db_ciclo_escolar = crud.query_row_ciclo_escolar(db=db, id_ciclo_escolar=id_ciclo_escolar)
    if db_ciclo_escolar is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_ciclo_escolar
"""
@app.post("/ciclo_escolar/", tags = ["ciclo_escolar"], status_code=status.HTTP_202_ACCEPTED)
async def create_ciclo_escolar(ciclo_base: schemas.WOICicloEscolarBase, db: Session = Depends(get_db)):
    if crud.insert_row_ciclo_escolar(db=db, ciclo_escolar=ciclo_base) is True:
        return {"message": "Ciclo Escolar agregado"}
    else:
        raise HTTPException(status_code=400, detail="No se agrego correctamente")

@app.put("/ciclo_escolar/", tags=["ciclo_escolar"], status_code=status.HTTP_202_ACCEPTED)
async def update_ciclo_escolar(ciclo_escolar: schemas.CicloEscolarBase, db: Session = Depends(get_db)):
    if(crud.update_row_ciclo_escolar(db=db, ciclo_escolar=ciclo_escolar)) is True:
        return {"message": "Ciclo Escolar actualizado"}
    else:
        raise HTTPException(status_code=400, detail="No se actualizo correctamente")

@app.delete("/ciclo_escolar/{id_ciclo_escolar}", tags=["ciclo_escolar"], status_code=status.HTTP_202_ACCEPTED)
async def delete_ciclo_escolar(id_ciclo_escolar: int, db: Session = Depends(get_db)):
    if crud.delete_row_ciclo_escolar(db=db, id_ciclo_escolar=id_ciclo_escolar) is True:
        return {"message": "Ciclo Escolar eliminado"}
    else:
        raise HTTPException(status_code=400, detail="No se elimino correctamente")


"""@app.get("/ciclo_escolar/", tags = ["ciclo_escolar"], status_code=status.HTTP_202_ACCEPTED,
response_model=List[schemas.CicloEscolarBase])
async def read_ciclo_escolar(db: Session = Depends(get_db)):
    db_ciclo_escolar = crud.query_all_ciclo_escolar(db=db)
    if db_ciclo_escolar is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_ciclo_escolar """


@app.get("/carrera/{id_carrera}", tags = ["carreras"], status_code=status.HTTP_202_ACCEPTED,
response_model=schemas.CarrerasBase)
async def read_carrera(id_carrera: int, db: Session = Depends(get_db)):
    db_carrera = crud.query_row_carreras(db=db, id_carrera=id_carrera)
    if db_carrera is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_carrera

@app.post("/carrera/", tags = ["carreras"], status_code=status.HTTP_202_ACCEPTED)
async def create_carrera(carrera: schemas.WOICarrerasBase, db: Session = Depends(get_db)):
    if crud.insert_row_carreras(db=db, carrera=carrera) is True:
        return {"message": "Carrera agregada"}
    else:
        raise HTTPException(status_code=400, detail="No se agrego correctamente")

@app.put("/carrera/", tags=["carreras"], status_code=status.HTTP_202_ACCEPTED)
async def update_carrera(carrera: schemas.CarrerasBase, db: Session = Depends(get_db)):
    if(crud.update_row_carreras(db=db, carrera=carrera)) is True:
        return {"message": "Carrera actualizada"}
    else:
        raise HTTPException(status_code=400, detail="No se actualizo correctamente")

@app.delete("/carrera/{id_carrera}", tags=["carreras"], status_code=status.HTTP_202_ACCEPTED)
async def delete_carrera(id_carrera: int, db: Session = Depends(get_db)):
    if crud.delete_row_carreras(db=db, id_carrera=id_carrera) is True:
        return {"message": "Carrera eliminada"}
    else:
        raise HTTPException(status_code=400, detail="No se elimino correctamente")


@app.get("/planestudios/{id_plan_estudios}", tags = ["plan de estudios"], status_code=status.HTTP_202_ACCEPTED,
response_model=schemas.PlanEstudiosBase)
async def read_plan_estudios(id_plan_estudios: int, db: Session = Depends(get_db)):
    db_plan_estudios = crud.query_row_plan_estudios(db=db, id_plan_estudios=id_plan_estudios)
    if db_plan_estudios is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_plan_estudios

@app.post("/planestudios/", tags = ["plan de estudios"], status_code=status.HTTP_202_ACCEPTED)
async def create_plan_estudios(plan_estudios: schemas.WOIPlanEstudiosBase, db: Session = Depends(get_db)):
    if crud.insert_row_plan_estudios(db=db, plan_estudios=plan_estudios) is True:
        return {"message": "Plan de estudios agregado"}
    else:
        raise HTTPException(status_code=400, detail="No se agrego correctamente")

@app.put("/planestudios/", tags=["plan de estudios"], status_code=status.HTTP_202_ACCEPTED)
async def update_plan_estudios(plan_estudios: schemas.PlanEstudiosBase, db: Session = Depends(get_db)):
    if(crud.update_row_plan_estudios(db=db, plan_estudios=plan_estudios)) is True:
        return {"message": "Plan de estudios actualizado"}
    else:
        raise HTTPException(status_code=400, detail="No se actualizo correctamente")

@app.delete("/planestudios/{id_plan_estudios}", tags=["plan de estudios"], status_code=status.HTTP_202_ACCEPTED)
async def delete_plan_estudios(id_plan_estudios: int, db: Session = Depends(get_db)):
    if crud.delete_row_plan_estudios(db=db, id_plan_estudios=id_plan_estudios) is True:
        return {"message": "Plan de estudios eliminado"}
    else:
        raise HTTPException(status_code=400, detail="No se elimino correctamente")


@app.get("/turnos/{id_turno}", tags = ["turnos"], status_code=status.HTTP_202_ACCEPTED,
response_model=schemas.TurnosBase)
async def read_turnos(id_turno: int, db: Session = Depends(get_db)):
    db_turnos = crud.query_row_turnos(db=db, id_turno=id_turno)
    if db_turnos is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_turnos

@app.post("/turnos/", tags = ["turnos"], status_code=status.HTTP_202_ACCEPTED)
async def create_turnos(turnos: schemas.WOITurnosBase, db: Session = Depends(get_db)):
    if crud.insert_row_turnos(db=db, turnos=turnos) is True:
        return {"message": "Turno agregado"}
    else:
        raise HTTPException(status_code=400, detail="No se agrego correctamente")

@app.put("/turnos/", tags=["turnos"], status_code=status.HTTP_202_ACCEPTED)
async def update_turnos(turnos: schemas.TurnosBase, db: Session = Depends(get_db)):
    if(crud.update_row_turnos(db=db, turnos=turnos)) is True:
        return {"message": "Turno actualizado"}
    else:
        raise HTTPException(status_code=400, detail="No se actualizo correctamente")

@app.delete("/turnos/{id_turno}", tags=["turnos"], status_code=status.HTTP_202_ACCEPTED)
async def delete_turnos(id_turno: int, db: Session = Depends(get_db)):
    if crud.delete_row_turnos(db=db, id_turno=id_turno) is True:
        return {"message": "Turno eliminado"}
    else:
        raise HTTPException(status_code=400, detail="No se elimino correctamente")

















    
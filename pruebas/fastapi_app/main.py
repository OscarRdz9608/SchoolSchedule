"""coding=utf-8."""
 
from typing import List
 
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
 
from . import crud, models, schemas
from .database import SessionLocal, engine
 
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

@app.get("/usuarios/{email}", tags = ["usuarios"], status_code=status.HTTP_202_ACCEPTED)
async def read_user(email: str, db: Session = Depends(get_db)):
    db_user = crud.query_row_Usuarios(db=db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user

@app.post("/usuarios/", tags = ["usuarios"], status_code=status.HTTP_202_ACCEPTED)
async def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    if crud.insert_row_Usuarios(db=db, user_base=user) is True:
        return {"message": "Usuario agregado"}
    else:
        raise HTTPException(status_code=400, detail="Correo ya registrado")

@app.get("/ciclo_escolar/{id_ciclo_escolar}", tags = ["ciclo_escolar"], status_code=status.HTTP_202_ACCEPTED,
response_model=schemas.CicloEscolarBase)
async def read_ciclo_escolar(id_ciclo_escolar: int, db: Session = Depends(get_db)):
    db_ciclo_escolar = crud.query_row_ciclo_escolar(db=db, id_ciclo_escolar=id_ciclo_escolar)
    if db_ciclo_escolar is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_ciclo_escolar
"""coding=utf-8."""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:12345678@localhost:5432/pruebas_horarios"

SQLALCHEMY_DATABASE_URL = "postgresql://oscarrm:password123@localhost:5432/oscarrm"
 
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
Base = declarative_base()
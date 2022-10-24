"""coding=utf-8."""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:12345678@localhost:5432/horarios"

SQLALCHEMY_DATABASE_URL =  "postgresql://postgres:26Ti9228twc8!d3@db.svhulthwokfuuwlasvul.supabase.co:5432/postgres"
 
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
Base = declarative_base()
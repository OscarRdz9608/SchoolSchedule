from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine=create_engine("postgresql://oscarrm:password123@localhost:5432/oscarrm",
    echo=True
)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)
from database import Base,engine
import models

try: 
    print("Creating database ....")
    Base.metadata.create_all(engine)
except Exception as error: 
    print(error)
    
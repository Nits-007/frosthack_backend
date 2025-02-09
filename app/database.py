from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'postgresql://frosthacks_uy3a_user:Ias6xcVHKmU4dhSGbBP0tAzhiRQXFaWd@dpg-cujvsa0gph6c73bma9bg-a/frosthacks_uy3a'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db(): 
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

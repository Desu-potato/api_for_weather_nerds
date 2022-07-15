from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_NAME = "fastapi"
DB_USER = "postgres"
DB_PASSWORD = "1234"
SQL_DB_URL = "postgresql://{}:{}@{}/{}".format(DB_USER,DB_PASSWORD, "Localhost", DB_NAME)


engine = create_engine(SQL_DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
         db.close()

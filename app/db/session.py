from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os

SQL_DB_CONN = os.getenv("DB_CONN")

engine = create_engine(SQL_DB_CONN)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
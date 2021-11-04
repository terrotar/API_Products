from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///api/Database/sql_api.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"


# Sqlite3, by default, set one connection per thread to avoid the possibility
# of 2 or more conn do the same request to database... BUT, using functions in
# FastAPI, it's normal that it happens a lot, so we need to set that args
# inside engine

# Obs: Only Sqlite3 nedd that configuration due to be the only one who does it
engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       connect_args={"check_same_thread": False}
                       )


# Make sessions with database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# All classes will inherit Base to map them inside ORM
Base = declarative_base()

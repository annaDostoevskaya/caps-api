import os
from fastapi import FastAPI
from config import Config
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

app = FastAPI()
conf = Config()

# NOTE(annad): `Base.metadata.create_all(DBEngine)` for add in base tables, ORM.
Base = declarative_base()
DBEngine = create_engine(conf.SQLALCHEMY_DATABASE_URL, echo=True,)
DBSession = sessionmaker(
    binds = {
        Base: DBEngine
    },
    expire_on_commit=False
)


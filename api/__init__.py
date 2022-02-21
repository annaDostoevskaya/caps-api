import os
from fastapi import FastAPI
from config import Config
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

app = FastAPI()
app.description = 'It\'s CapsApi, API for internet shop of caps'

conf = Config()

# from dev.vkauth_test import *

## NOTE(annad): `Base.metadata.create_all(DBEngine)` for add in base tables, ORM.
Base = declarative_base()
DBEngine = create_engine(conf.SQLALCHEMY_DATABASE_URL, echo=conf.SQLALCHEMY_ECHO)
DBSession = sessionmaker(
    binds = {
        Base: DBEngine
    },
    expire_on_commit=False
)


import os
from fastapi import FastAPI
from config import Config
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

app = FastAPI()
conf = Config()

Base = declarative_base()
DBEngine = create_engine(conf.SQLALCHEMY_DATABASE_URL, echo=True,)
DBSession = sessionmaker(
    binds = {
        Base: DBEngine
    },
    expire_on_commit=False
)



import os

import sqlalchemy as db
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import Column, Integer, String, Boolean

load_dotenv()
ip = str(os.getenv("IP"))
pguser = str(os.getenv("PGUSER"))
password = str(os.getenv("PGPASS"))
database = str(os.getenv("DATABASE"))

engine = db.create_engine(f"postgresql+psycopg2://{pguser}:{password}@{ip}/{database}")
session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = session.query_property()
connection = engine.connect()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    name = Column(String)
    admin = Column(Boolean, default=False)
    telegram_id = Column(Integer)


class Question(Base):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True)
    text = Column(String)


Base.metadata.create_all(bind=engine)

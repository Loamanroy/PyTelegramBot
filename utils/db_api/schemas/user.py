import sqlalchemy
from sqlalchemy import Column, BigInteger, String, sql

from utils.db_api.db_telegrambot import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True)
    firstname = Column(String(200))
    lastname = Column(String(200))
    username = Column(String(50))
    status = Column(String(30))

    query: sql.select
    
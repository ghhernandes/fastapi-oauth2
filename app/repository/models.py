from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    nickname = Column(String(20))
    fullname = Column(String(100))
    hashed_password = Column(String(255))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

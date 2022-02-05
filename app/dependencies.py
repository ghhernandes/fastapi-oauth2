from sqlalchemy.orm import Session

from .repository import db


def get_db() -> Session:
    database = db.DB()
    return database.LocalSession()
    


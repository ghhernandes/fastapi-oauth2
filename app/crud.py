from xmlrpc.client import Boolean
from sqlalchemy.orm import Session

from . import schemas
from .repository import models

def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    user_db = models.User(**user.dict())
    db.add(user_db)
    db.commit()
    return user_db

def remove_user(db: Session, user_id: int) -> None:
    user_db = db.query(models.User).filter(models.User.id == user_id).first()
    if user_db:
        db.delete(user_db)
        db.commit()

def list_all_users(db: Session) -> list[models.User]:
    return db.query(models.User).all()

def get_user_by_nickname(db: Session, nickname: str) -> models.User:
    return db.query(models.User).filter(models.User.nickname == nickname).first()
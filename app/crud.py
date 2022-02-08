from fastapi import Depends
from sqlalchemy.orm import Session

from . import schemas
from . import dependencies
from .repository import models

def get_user_by_nickname(db: Session, nickname: str) -> models.User:
    return db.query(models.User).filter(models.User.nickname == nickname).first()

def get_current_user(db: Session, token: str = Depends(dependencies.oauth2_scheme)) -> models.User:
    token_data: schemas.TokenData = dependencies.get_token_data(token)
    user_db = get_user_by_nickname(token_data.nickname)
    if not user_db:
        return False
    return user_db

def authenticate_user(db: Session, nickname: str, password: str) -> models.User:
    user_db: models.User = get_user_by_nickname(db, nickname)
    if not user_db:
        return False
    if not dependencies.verify_password(password, user_db.hashed_password):
        return False
    return user_db

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
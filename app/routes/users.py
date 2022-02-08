from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import crud
from ..schemas import User, UserCreate
from ..dependencies import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("/", response_model=User | list)
async def list_users(db: Session = Depends(get_db)):
    return crud.list_all_users(db)  

# @router.get("/{user_id}", response_model=User | list)
# async def get_id(user_id: int):
#     pass


@router.post("/", response_model=User | list)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)
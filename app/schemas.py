from pydantic import BaseModel

class User(BaseModel):
    id: int
    nickname: str
    fullname: str
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    nickname: str
    fullname: str
    password: str
    class Config:
        orm_mode = True
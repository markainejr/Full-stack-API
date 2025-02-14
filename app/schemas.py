from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from typing_extensions import Annotated
from datetime import datetime



class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
        id: int
        email : EmailStr
        created_at: datetime


class Post(PostBase):
    id : int
    created_at: datetime
    owner_id : int
    owner: UserOut


    class Config:   #it can be optional
        orm_mode = True

class UserCreate(BaseModel):
    email : EmailStr
    password:str

class UserOut(BaseModel):
        id: int
        email : EmailStr
        created_at: datetime

class UserLogin(BaseModel):
     email: EmailStr
     password: str


class Token(BaseModel):
     access_Token: str
     token_type: str

class TokenData(BaseModel):
     id :Optional[str] = None


class Vote(BaseModel):
     post_id: int
     dir: Annotated[int, Field(strict = True, le = 1)]

     
     
        






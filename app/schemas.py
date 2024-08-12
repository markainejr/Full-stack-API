from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime



class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass


class Post(PostBase):
    id : int
    created_at: datetime


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

     
     
        






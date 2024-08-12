from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from sqlalchemy.sql.expression import text
from .database import Base


class Post(Base): #sqlalchemy model
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable = False)
    content = Column(String, nullable = False)
    published = Column(Boolean, server_default = 'TRUE')
    created_at = Column(TIMESTAMP (timezone= True), server_default = text('now()'))

class User(Base):
    __tablename__= "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)
    created_at = Column(TIMESTAMP (timezone= True), server_default = text('now()'), nullable = False)

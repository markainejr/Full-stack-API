from fastapi import FastAPI, Body, status, HTTPException, Depends, Response
from pydantic import BaseModel

from typing import Optional, List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models, schemas, utilis
from .database import engine,  get_db
from .routers import post, user,auth





models.Base.metadata.create_all(bind= engine)

app = FastAPI()





while True:
    try:
        conn = psycopg2.connect(host='localhost', database='FastApidb', user='postgres', password='password1', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        print("Connecting to a Database failed")
        print("Error:", error)
        time.sleep(2)


    


my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {
    "title": "favorite foods", "content": "i like piiza", "id": 2}]


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
        
def find_index_post(id):
    for i, p in enumerate (my_posts):
        if p['id'] == id:
            return i
        

app.include_router(
    post.router

)

app.include_router(
    user.router

)

app.include_router(
    auth.router

)


@app.get("/")
def root():
    return {"message": "hello world"}




    



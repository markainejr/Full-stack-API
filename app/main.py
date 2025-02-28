from fastapi import FastAPI
from pydantic import BaseModel
from .config import settings
from fastapi.middleware.cors import CORSMiddleware


from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user, auth, vote



app = FastAPI()

# Include your routers here
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





#models.Base.metadata.create_all(bind= engine) we dont need it since alembic is creating the tables

app = FastAPI()




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




    



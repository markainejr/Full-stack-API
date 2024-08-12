from fastapi import FastAPI, Body, status, HTTPException, Depends, Response, APIRouter, APIRouter
from typing import List


from .. import models, schemas, oauth2
from sqlalchemy.orm import Session
from .. database import   get_db


router = APIRouter(
    prefix= "/posts",
    tags= ["Posts"]

)








@router.get("/", response_model= List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
     posts = db.query(models.Post).all()
     #cursor.execute("""SELECT * FROM posts""")
     #posts =cursor.fetchall()
     return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: schemas.TokenData = Depends(oauth2.get_current_user)):
    print(current_user.id)
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}",response_model= schemas.Post)
def get_post(id: int, db: Session = Depends(get_db)):
    #cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id),))
   # post = cursor.fetchone()
    post = db.query(models.Post).filter(models.Post.id ==id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with the id {id} does not exist")
    else:
        return  post


    
@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db:Session = Depends(get_db)):
     post = db.query(models.Post).filter(models.Post.id ==id)
     if post.first() ==  None:
        raise HTTPException(status_code =status.HTTP_404_NOT_FOUND, detail=f"post with the id {id} does not exist")
     post.delete(synchronize_session = False)
     db.commit()
     return Response(status_code = status.HTTP_204_NO_CONTENT,  ) 
    
@router.put("/{id}", response_model= schemas.Post) 
def update_post(id: int, updated_post: schemas.PostCreate, db:Session = Depends(get_db)):
    #cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s  RETURNING *""", (post.title, post.content, post.published, id) )
    #updated_post= cursor.fetchone()
    post_query= db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    db.commit()
    if post is None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND )
    else:
        post_query.update(updated_post.dict(), synchronize_session=False)
        db.commit()
        return  post_query.first()
from fastapi import FastAPI, Depends, status, Response, HTTPException,
import database
import models
import schemas
from database import engine, SessionLocal
from sqlalchemy.orm import Session

models.Base.metadata.create_all(engine)

app = FastAPI()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@app.get("/blog")
def all(db: Session = Depends (get_db)):
  # to get all the data from a Table
  blogs = db.query(models.Blog).all()
  return blogs

@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends (get_db)):
  new_blog = models.Blog(title=request.title, body=request.body)
  db.add(new_blog)
  db.commit()
  db.refresh(new_blog)
  return new_blog

@app.get("/blog/{id}")
def getOne(id, Response:Response, db: Session = Depends (get_db)):
  # here filter works like where clause in sql
  blog = db.query(models.Blog).filter(models.Blog.id == id).first()

  if not blog:
    Response.status_code = status.HTTP_404_NOT_FOUND
    return {'detail': f"Blog with the id {id} is not available"}

  return blog


@app.get("/blog/{id}")
def getOne(id, Response:Response, db: Session = Depends (get_db)):
  # here filter works like where clause in sql
  blog = db.query(models.Blog).filter(models.Blog.id == id).first()

  if not blog:
    HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail: f"Blog with the id {id} is not available")
  return blog
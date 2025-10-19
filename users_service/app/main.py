from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .db import SessionLocal, init_db
from . import models, schemas

app = FastAPI(title="Users Service", version="1.0.0")

@app.on_event("startup")
def on_startup():
 init_db()
def get_db():
 db = SessionLocal()
 try:
    yield db
 finally:
    db.close()

@app.post("/users", response_model=schemas.UserOut, status_code=201)
def create_user(payload: schemas.UserCreate, db: Session = Depends(get_db)):
 exists = db.query(models.User).filter_by(email=payload.email).first()
 if exists:
    raise HTTPException(status_code=409, detail="email already exists")
 user = models.User(name=payload.name, email=payload.email)
 db.add(user)
 db.commit()
 db.refresh(user)
 return user

@app.get("/users", response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(get_db)):
 return db.query(models.User).order_by(models.User.id).all()

@app.get("/users/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
 user = db.query(models.User).get(user_id)
 if not user:
    raise HTTPException(status_code=404, detail="user not found")
 return user
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .db import SessionLocal, init_db
from . import models, schemas
from .clients import user_exists

app = FastAPI(title="Orders Service", version="1.0.0")

@app.on_event("startup")
def on_startup():
 init_db()

def get_db():
 db = SessionLocal()
 try:
    yield db
 finally:
    db.close()

@app.post("/orders", response_model=schemas.OrderOut, status_code=201)
def create_order(payload: schemas.OrderCreate, db: Session = Depends(get_db)):
 if not user_exists(payload.user_id):
    raise HTTPException(status_code=422, detail="user_id does not exist in users_service")
 order = models.Order(user_id=payload.user_id, item=payload.item, qty=payload.qty)
 db.add(order)
 db.commit()
 db.refresh(order)
 return order

@app.get("/orders", response_model=list[schemas.OrderOut])
def list_orders(db: Session = Depends(get_db)):
 return db.query(models.Order).order_by(models.Order.id).all()

@app.get("/orders/{order_id}", response_model=schemas.OrderOut)
def get_order(order_id: int, db: Session = Depends(get_db)):
 order = db.query(models.Order).get(order_id)
 if not order:
    raise HTTPException(status_code=404, detail="order not found")
 return order

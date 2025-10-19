from sqlalchemy import Column, Integer, String
from .db import Base

class Order(Base):
 __tablename__ = "orders"
 id = Column(Integer, primary_key=True, index=True)
 user_id = Column(Integer, index=True, nullable=False)
 item = Column(String(120), nullable=False)
 qty = Column(Integer, nullable=False, default=1)

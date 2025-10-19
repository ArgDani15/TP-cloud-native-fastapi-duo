from pydantic import BaseModel, Field

class OrderCreate(BaseModel):
 user_id: int = Field(gt=0)
 item: str
 qty: int = Field(gt=0, le=1000)

class OrderOut(BaseModel):
 id: int
 user_id: int
 item: str
 qty: int
 class Config:
    from_attributes = True

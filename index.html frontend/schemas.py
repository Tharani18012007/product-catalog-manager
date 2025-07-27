# schemas.py
from pydantic import BaseModel

class ProductBase(BaseModel):
    title: str
    description: str
    price: float
    category: str

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        from_attributes=True


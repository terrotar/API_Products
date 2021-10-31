
from pydantic import BaseModel


# Base's schemas has common attributes, as for reading
# or writting(creating)
class ProductBase(BaseModel):
    name: str
    description: str
    price: float


# Attributes only when instance the object
class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    # Configuration to enable search like attributes instead of
    # only dict and access tables mapped in ORM SQLAlchemy
    # Product.name instead of Product["name"]

    class Config:
        orm_mode = True

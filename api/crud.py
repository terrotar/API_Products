
from sqlalchemy.orm import Session

# ORM Classes/Tables
from Database import models


# Pydantic Schemas
from Pydantic import schemas


# Get product by id
def get_product_by_id(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


# Get product by name
def get_product_by_name(db: Session, product_name: str):
    return db.query(models.Product).filter(models.Product.name == product_name).first()


# Sets a limit of qtd items(100) to the response
def get_all_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


# Create a product object
def create_product(db: Session, product: schemas.ProductCreate):
    new_product = models.Product(name=product.name,
                                 description=product.description,
                                 price=product.price)
    db.add(new_product)
    db.commit()
    # Update database with the new object
    db.refresh(new_product)
    return new_product

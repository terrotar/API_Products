
from typing import Optional

from sqlalchemy.orm import Session

# ORM Classes/Tables
from api.Database import models


# Pydantic Schemas
from api.Pydantic import schemas


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


# Delete a product by it's id
def delete_product(db: Session, product_id: int):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product


# Update a product's name
def update_product_name(db: Session, product: schemas.Product, product_name: str):
    if product:
        product.name = product_name
        db.commit()
        db.refresh(product)
        return product


# Update a product's description
def update_product_description(db: Session, product: schemas.Product, product_description: str):
    if product:
        product.description = product_description
        db.commit()
        db.refresh(product)
        return product


# Update a product's price
def update_product_price(db: Session, product: schemas.Product, product_price: float):
    if product:
        product.price = product_price
        db.commit()
        db.refresh(product)
        return product

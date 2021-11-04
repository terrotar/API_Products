
from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
from Database import models
from Database.database import SessionLocal, engine
from Pydantic import schemas


# Create all tables mapped with ORM
models.Base.metadata.create_all(bind=engine)


# Instance of FastAPI
api = FastAPI()


# Dependency of Session's Database
# With that, the entire API will consume only one session per request
# and closes it right after the query's result

# Obs: the function uses 'try:' because if happens to occur some error
# in the middle, and error output or exception(if included) will raise
# Also, the 'finally:' ensures that the connection wil lbe closed in the
# end of function get_db()
def get_db():
    # Creates a session query
    db = SessionLocal()
    try:
        # Wait until it's used
        yield db
    finally:
        # Close the connection
        db.close()


# Create object Product
@api.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_name(db, product_name=product.name)
    if db_product:
        raise HTTPException(
            status_code=400, detail="Product's name already registered")
    return crud.create_product(db=db, product=product)


# Get all Products
@api.get("/products/", response_model=List[schemas.Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    all_products = crud.get_all_products(db, skip=skip, limit=limit)
    return all_products


# Get a Product by id
@api.get("/product/id/{product_id}", response_model=schemas.Product)
def read_product_by_id(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_id(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


# Get a Product by name
@api.get("/products/name/{product_name}", response_model=schemas.Product)
def read_product_by_name(product_name: str, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_name(db, product_name=product_name)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


# Delete a Product by it's id
@api.delete("/delete/product/{product_id}", response_model=schemas.Product)
def delete_product_by_id(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_id(db, product_id=product_id)
    if db_product:
        db_product = crud.delete_product(db, product_id=product_id)
        return db_product
    raise HTTPException(status_code=404, detail="Product not found")


# Update a product by it's id
@api.patch("/update/product/{product_id}", response_model=schemas.Product)
def update_product(product_id: int,
                   product_name: Optional[str] = None,
                   product_description: Optional[str] = None,
                   product_price: Optional[float] = None,
                   db: Session = Depends(get_db)):
    db_product = crud.get_product_by_id(db, product_id=product_id)
    if db_product:
        if product_name:
            crud.update_product_name(db, db_product, product_name)
        if product_description:
            crud.update_product_description(db, db_product, product_description)
        if product_price:
            crud.update_product_price(db, db_product, product_price)
        return db_product
    raise HTTPException(status_code=404, detail="Product not found")


from fastapi import FastAPI

# Library to create Models and validations
from pydantic import BaseModel


# Instance of api
api = FastAPI()


# Product Model
class Product(BaseModel):
    Nome: str
    Descricao: str
    Preco: float


# Test Route of Product.Model
@api.get('/list/all_products')
def get_all_products():


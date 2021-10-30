from sqlalchemy import Column, Float, Integer, String

from .database import Base


class Product(Base):
    __tablename__ = "Produto"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(30), unique=True, index=True)
    description = Column(String(60), index=True)
    price = Column(Float, index=True)

# app/models/product.py
from sqlalchemy import Column, Float, Integer, MetaData, String
from sqlalchemy.orm import declarative_base

metadata = MetaData(schema="ecommerce_schema")
Base = declarative_base(metadata=metadata)  # type: ignore


class Product(Base):  # type: ignore
    """Model for products."""

    __tablename__ = "product"

    product_id = Column("product_id", Integer, primary_key=True)
    name = Column("name", String(200))
    description = Column("description", String(500))
    price = Column("price", Float)
    stock_count = Column("stock_count", Integer)
    category = Column("category", String(100))
    parent_product_id = Column("parent_product_id", Integer)

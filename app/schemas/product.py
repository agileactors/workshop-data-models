from typing import Optional

from pydantic import BaseModel


class ProductSchema(BaseModel):
    """Schema for products."""

    product_id: int
    name: str
    description: str
    price: float
    stock_count: int
    category: str
    parent_product_id: Optional[int]

    class Config:
        """Pydantic configuration."""

        from_orm = True
        from_attributes = True

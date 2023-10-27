from sqlalchemy import select

from app.models.product import Product
from app.schemas.product import ProductSchema
from app.services.base import BaseDataManager, BaseService


class ProductService(BaseService):
    """Service responsible for operations over products."""

    def get_product(self, product_id: int) -> ProductSchema:
        """Get product by ID."""

        return ProductDataManager(self.session).get_product(product_id)


class ProductDataManager(BaseDataManager):
    """Data manager responsible for operations over products."""

    def get_product(self, product_id: int) -> ProductSchema:
        """Get product by ID."""

        stmt = select(Product).where(Product.product_id == product_id)
        model = self.get_one(stmt)
        return ProductSchema.from_orm(model)

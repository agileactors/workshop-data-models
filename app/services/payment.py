from sqlalchemy import select

from app.models.payment import Payment
from app.schemas.payment import PaymentSchema
from app.services.base import BaseDataManager, BaseService


class PaymentService(BaseService):
    """Service responsible for operations over payments."""

    def get_all_payments(self) -> list[PaymentSchema]:
        """Retrieve all payments from the database."""

        return PaymentDataManager(self.session).get_all_payments()


class PaymentDataManager(BaseDataManager):
    """Data manager responsible for operations over payments."""

    def get_all_payments(self) -> list[PaymentSchema]:
        """Retrieve all payments from the database."""

        stmt = select(Payment)
        models = self.get_all(stmt)
        return [PaymentSchema.from_orm(model) for model in models]

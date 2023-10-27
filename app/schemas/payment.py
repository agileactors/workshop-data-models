from datetime import date

from pydantic import BaseModel


class PaymentSchema(BaseModel):
    """Schema for payments."""

    payment_id: int
    order_id: int
    payment_method: str
    payment_date: date
    amount: float

    class Config:
        """Pydantic configuration."""

        from_orm = True
        from_attributes = True

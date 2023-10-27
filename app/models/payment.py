from sqlalchemy import Column, Date, Float, Integer, MetaData, String
from sqlalchemy.orm import declarative_base

metadata = MetaData(schema="ecommerce_schema")
Base = declarative_base(metadata=metadata)  # type: ignore


class Payment(Base):  # type: ignore
    """Model for payment."""

    __tablename__ = "payment"

    payment_id = Column("payment_id", Integer, primary_key=True)
    order_id = Column("order_id", Integer)
    payment_method = Column("payment_method", String(50))
    payment_date = Column("payment_date", Date)
    amount = Column("amount", Float)

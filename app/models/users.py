from sqlalchemy import Column, Date, Integer, MetaData, String
from sqlalchemy.orm import declarative_base

metadata = MetaData(schema="ecommerce_schema")
Base = declarative_base(metadata=metadata)  # type: ignore


class Users(Base):  # type: ignore
    """Model for users."""

    __tablename__ = "users"

    user_id = Column("user_id", Integer, primary_key=True)
    username = Column("username", String)
    password = Column("password", String)
    email = Column("email", String)
    registration_date = Column("registration_date", Date)
    user_type = Column("user_type", String)

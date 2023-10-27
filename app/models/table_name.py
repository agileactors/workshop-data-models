from sqlalchemy import Column, Float, Integer, MetaData, String
from sqlalchemy.orm import declarative_base

metadata = MetaData(schema="test_schema")
Base = declarative_base(metadata=metadata)  # type: ignore


class TableNameModel(Base):  # type: ignore
    """Model for table_name."""

    __tablename__ = "test_table"

    column_name_1 = Column("column_name_1", Integer, primary_key=True)
    column_name_2 = Column("column_name_2", String(200))
    column_name_3 = Column("column_name_3", Float)

from pydantic import BaseModel


class TableNameSchema(BaseModel):
    """Schema for table_name."""

    column_name_1: int
    column_name_2: str
    column_name_3: float

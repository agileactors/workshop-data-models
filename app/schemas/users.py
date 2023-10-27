from datetime import date

from pydantic import BaseModel


class UsersSchema(BaseModel):
    """Schema for users."""

    user_id: int
    username: str
    password: str
    email: str
    registration_date: date
    user_type: str

    class Config:
        """Pydantic configuration."""

        from_orm = True
        from_attributes = True


class UserCreateSchema(BaseModel):
    """Schema for creating users."""

    username: str
    password: str
    email: str
    user_type: str

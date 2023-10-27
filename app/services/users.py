from datetime import date

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app.models.users import Users
from app.schemas.users import UserCreateSchema, UsersSchema
from app.services.base import BaseDataManager, BaseService


class DuplicateEmailError(Exception):
    """Raised when trying to add a user with a duplicate email."""

    pass


class UsersService(BaseService):
    """Service responsible for operations over users."""

    def get_all_users(self) -> list[UsersSchema]:
        """Retrieve all users from the database."""

        return UsersDataManager(self.session).get_all_users()

    def add_user(self, user_data: UserCreateSchema) -> UsersSchema:
        """Add a new user to the database."""

        user = Users(**user_data.dict(), registration_date=date.today())
        try:
            added_user = UsersDataManager(self.session).add_one(user)
            return UsersSchema.from_orm(added_user)
        except IntegrityError as error_message:
            raise DuplicateEmailError("Email already exists") from error_message


class UsersDataManager(BaseDataManager):
    """Data manager responsible for operations over users."""

    def get_all_users(self) -> list[UsersSchema]:
        """Retrieve all users from the database."""

        stmt = select(Users)
        models = self.get_all(stmt)
        return [UsersSchema.from_orm(model) for model in models]

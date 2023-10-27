import logging

from app.backend.session import create_session
from app.schemas.users import UserCreateSchema
from app.services.users import DuplicateEmailError, UsersService


def run():
    """Demonstrates how to use the UsersService to retrieve and add users."""

    with create_session() as session:
        users_service = UsersService(session)

        try:
            # Adding a user
            new_user_data = UserCreateSchema(
                username="new_user", password="new_password", email="new.user@example.com", user_type="customer"
            )
            added_user = users_service.add_user(new_user_data)
            logging.info(f"Added User ID: {added_user.user_id} - Username: {added_user.username} - Email: {added_user.email}")
        except DuplicateEmailError:
            logging.error("Error: Email already exists")

        # Retrieve all users
        all_users = users_service.get_all_users()
        for user in all_users:
            logging.info(f"User ID: {user.user_id} - Username: {user.username} - Email: {user.email}")

# This file contains the class for user managenment.
from database_model.user_repository import UserRepository


class UserManagenment:

    def create_user(
        username: str,
        money: str = "0",
        territory: str = "0",
        buildings: str = "0",
    ) -> None:
        """Create user in database."""
        UserRepository(username, money, territory, buildings).upser_user_data()

    def update_user(
        username: str,
        money: str = "0",
        territory: str = "0",
        buildings: str = "0",
    ) -> None:
        """Update user data in database."""
        UserRepository(username, money, territory, buildings).upser_user_data()

    def delete_user(username) -> None:
        """Delete user from database."""
        UserRepository(username).delete_user()

    def get_user(username) -> dict | None:
        """
        Retrieve user data based on the provided username.
        Args:
            username (str): The username of the user to retrieve.
        Returns:
            dict or None: A dictionary containing user data if the user exists,
                          otherwise None.
        """

        user_data = UserRepository(username).get_user_data()
        if not user_data:
            return None
        return user_data

    def check_user_exist(username):
        """Check user existance in database."""
        user_data = UserRepository(username).get_user_data()
        if not user_data:
            return False
        return True

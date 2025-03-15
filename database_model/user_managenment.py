# This file contains the class for user managenment.
from database_model.user_repository import UserRepository


class UserManagenment:
    def __init__(self):
        pass

    def create_user(self, username: str, money: str = "0", territory: str = "0", buildings: str = "0"):
        UserRepository(username, money, territory, buildings).upser_user_data()

    def update_user(self, username: str, money: str = "0", territory: str = "0", buildings: str = "0"):
        UserRepository(username, money, territory, buildings).upser_user_data()

    def delete_user(self, username):
        UserRepository(username).delete_user()
            
    def get_user_data(self, username):
        user_data = UserRepository(username).get_user_data()
        if not user_data:
            return None
        return user_data

    def check_user_exit(self, username):
        """Check user existance in database."""
        user_data = UserRepository(username).get_user_data()
        if not user_data:
            return False
        return True


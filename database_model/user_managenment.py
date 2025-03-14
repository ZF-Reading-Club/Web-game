
from database_model.delete_user import DeleteUser
from database_model.get_user import GetUser
from database_model.upsert_user import UpsertUser


class UserManagenment:
    def __init__(self):
        pass

    def create_user(self, username: str, money: str = "0", territory: str = "0", buildings: str = "0"):
        UpsertUser(username, money, territory, buildings).upsert_user()

    def update_user(self, username: str, money: str = "0", territory: str = "0", buildings: str = "0"):
        UpsertUser(username, money, territory, buildings).upsert_user()

    def delete_user(self, username):
        DeleteUser(username).delete_user()
            
    def get_user_data(self, username):
        user_data = GetUser(username).get_user_data()
        if not user_data:
            return None
        return user_data

    def check_user_exit(self, username):
        """Check user existance in database."""
        user_data = GetUser(username).get_user_data()
        if not user_data:
            return False
        return True


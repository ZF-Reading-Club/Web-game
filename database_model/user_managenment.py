
class UserManagenment():
    def __init__(self):
        pass

    def create_user(self, username, password):
        pass

    def update_user(self, username, password):
        pass

    def delete_user(self, username):
        pass


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


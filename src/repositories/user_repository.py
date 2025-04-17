import sys
import logging

import bcrypt

from models.users import UserTable
from models.database_context import DatabaseContext

logging.basicConfig(level=logging.DEBUG)


class UserRepository:
    def __init__(
        self, name: str, password: str = "", money: str = "", territory: str = "", buildings: str = ""
    ) -> None:
        """
        Initializes a new instance of the user repository.
        Args:
            name (str): The name of the user.
            password (str, optional): The password of the user. Defaults to an empty string.
            money (str, optional): The amount of money the user has. Defaults to an empty string.
            territory (str, optional): The territory owned by the user. Defaults to an empty string.
            buildings (str, optional): The buildings owned by the user. Defaults to an empty string.
        Attributes:
            data (dict): A dictionary to store user data.
            user_id (str): The unique identifier for the user.
            name (str): The name of the user.
            money (str): The amount of money the user has.
            territory (str): The territory owned by the user.
            buildings (str): The buildings owned by the user.
            session (Session): The database session for interacting with the database.
        """

        self.data = {}
        self.user_id = ""
        self.name = name
        self.password = password
        self.money = money
        self.territory = territory
        self.buildings = buildings
        database_context = DatabaseContext()
        database_context.initialize_database()
        self.session = database_context.session

    @staticmethod
    def _set_user_data(self) -> None:
        """
        Sets test data for the instance.
        This method populates the `data` attribute with predefined test values:
        - name
        - money
        - territory
        - buildings
        """

        self.data["name"] = self.name
        self.data["password"] = self._encode_psw(self.password)
        self.data["money"] = self.money
        self.data["territory"] = self.territory
        self.data["buildings"] = self.buildings
        self._check_data(self.data)
        logging.info(self.data)

    @staticmethod
    def _encode_psw(password: str) -> str:
        """
        Encodes the password using bcrypt hashing algorithm.
        Args:
            password (str): The password to be encoded.
        Returns:
            str: The encoded password.
        """
        psw_encoded = password.encode()  # always encode to bytes
        hashed = bcrypt.hashpw(psw_encoded, bcrypt.gensalt()) 
        return hashed.decode()  # decode to string    


    @staticmethod
    def _update_data(self, data) -> dict:
        """
        Updates the data attribute with the given data.
        Args:
            data (dict): A dictionary containing user data.
        Returns:
            dict: The updated data attribute.
        """
        data["money"] = int(data["money"]) + int(self.money)
        data["territory"] = int(data["territory"]) + int(self.money)
        data["buildings"] = int(data["buildings"]) + int(self.money)
        self._check_data(data)
        return data

    @staticmethod
    def _check_data(data):
        """
        Checks if the data is valid.
        Args:
            data (dict): A dictionary containing user data.
        """
        if (
            not data["name"]
            or not data["money"]
            or not data["territory"]
            or not data["buildings"]
        ):
            sys.exit(1)
        if int(data["money"]) < 0:
            sys.exit(1)
        if int(data["territory"]) < 0:
            sys.exit(1)
        if int(data["buildings"]) < 0:
            sys.exit(1)

    @staticmethod
    def _get_user_database_log(self):
        """
        Retrieves the database log for the user with the specified name.

        Returns:
            sqlalchemy.orm.query.Query: A query object to fetch the user data from the UserTable.
        """

        query = self.session.query(UserTable).filter_by(name=self.name)
        return query

    def upsert_user_data(self) -> None:
        """
        Adds data into the database.
        This method initializes the database context, creates a session, and attempts to add a new user record.
        Attributes:
            self.data (dict): A dictionary containing user data to be added to the database.
            self.user_id (int): The ID of the user added to the database.
        Returns:
            None
        """
        self._set_user_data()
        table = UserTable(**self.data)
        user_in_database = self._get_user_database_log()

        if not user_in_database.first():
            self.session.add(table)
            self.session.flush()
            self.user_id = table.id
            self.session.commit()
        else:
            logging.info(
                f"User {self.data} is already in database with ID {user_in_database.first().id} and its status will be changed"
            )
            data = user_in_database.first().__dict__
            data.pop("_sa_instance_state", None)
            data = self.update_data(data)
            self.session.query(UserTable).filter_by(
                id=user_in_database.first().id
            ).update(data)
            self.session.flush()
            self.session.commit()

    def get_user_data(self):
        """
        Retrieves user data from the database.
        This method fetches the first user log entry from the user database log.
        Returns:
            dict: A dictionary containing user data if the user is found in the database, otherwise None.
        """

        user_log = self._get_user_database_log().first()
        if not user_log:
            logging.info(f"User {self.name} is not in database")
            return None
        else:
            logging.info(
                f"User {self.name} is already in database with ID {user_log.id}."
            )
            data = user_log.__dict__
            data.pop("_sa_instance_state", None)
            return data

    def delete_user(self):
        """
        Deletes a user from the database.
        This method retrieves the user data from the database log. If the user exists,
        """

        user_data = self._get_user_database_log()
        if user_data.first():
            logging.warning(
                f"User {self.name} is going to be deleted from database."
                f"\n Data: {user_data.first().__dict__}"
            )
            user_data.delete()
            self.session.commit()
        else:
            logging.info(f"User {self.name} is not in database")

    def verify_user(self):
        """
        Verifies the user password.
        This method retrieves the user data from the database log and compares the provided password with the stored password.
        Returns:
            bool: True if the password is correct, False otherwise.
        """

        user_log = self._get_user_database_log().first()
        if not user_log:
            logging.info(f"User {self.name} is not in database")
            return False
        else:
            logging.info(
                f"User {self.name} is already in database with ID {user_log.id}."
            )
            data = user_log.__dict__
            data.pop("_sa_instance_state", None)
            if bcrypt.checkpw(self.password.encode(), data["password"].encode()):
                return True
            else:
                return False
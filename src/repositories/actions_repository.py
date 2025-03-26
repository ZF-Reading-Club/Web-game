import logging
import os
import sys
from src.models.database_context import DatabaseContext
from src.models.actions import ActionsTable

logging.basicConfig(level=logging.DEBUG)



class ActionsRepository:
    def __init__(self, user_id: str, building_type = None ,type=None, cooperation=None, against=None) -> None:
        """
        Initializes an instance of the actions repository.
        Args:
            user_id (str): The unique identifier for the user.
            type (optional): The type of action. Defaults to None.
            cooperation (optional): The cooperation parameter. Defaults to None.
            against (optional): The against parameter. Defaults to None.
        """

        self.actions = {}
        self.action_id = ""
        self.user_id = user_id
        self.type = type
        self.cooperation = cooperation
        self.against = against
        self.building_type = building_type
        database_context = DatabaseContext()
        database_context.initialize_database()
        self.session = database_context.session

    def _set_actions_data(self) -> None:
        """
        Update the `actions` dictionary with user data.
        """
        self.actions["user_id"] = self.user_id
        self.actions["type"] = self.type
        self.actions["cooperation"] = self.cooperation
        self.actions["against"] = self.against
        self.actions["building_type"] = self.building_type
        self._check_data(self.actions)

    @staticmethod
    def _check_data(data) -> None:
        """
        Validates the presence of 'user_id' and 'type' in the data. Logs an error and exits if missing.
        """
        if not data["user_id"] or not data["type"]:
            logging.error("Data is missing.")
            sys.exit(1)

    def _get_user_database_log(self, user_id=None) -> ActionsTable:
        """
        Retrieves the user database log from the ActionsTable.
        Args:
            user_id (int, optional): The ID of the user whose log is to be retrieved.
                If not provided, the method will use the instance's `user_id` and `type` attributes.
        Returns:
            ActionsTable: A query object representing the filtered results from the ActionsTable.
        """

        logging.info(f"User id: {user_id}")
        if user_id is not None:
            query = self.session.query(ActionsTable).filter_by(user_id=user_id)
        else:
            query = self.session.query(ActionsTable).filter_by(
                user_id=self.user_id, type=self.type
            )
        return query

    def set_actions_data(self) -> str:
        """
        Sets the actions data in the database.
        Returns:
            str: The ID of the actions data.
        """
        self._set_actions_data()
        table = ActionsTable(**self.actions)
        logging.info(f"User data: {self.actions}")
        actions_log_in_database = self._get_user_database_log()
        if actions_log_in_database.first() is not None:
            logging.info("User already exists in the database.")
            return actions_log_in_database.first()
        else:
            self.session.add(table)
            self.session.commit()
            self.session.flush()
            return table.id

    def get_user_actions_data(self) -> ActionsTable | None:
        """
        Retrieves the actions data from the database.
        Returns:
            ActionsTable: The actions data.
        """
        actions_log_in_database = self._get_user_database_log(self.user_id)
        logging.info(f"User data: {actions_log_in_database.first()}")
        if actions_log_in_database.first() is not None:
            return actions_log_in_database
        return None

    def delete_all_user_actions(self) -> bool:
        """
        Deletes all actions of a user from the database.
        Returns:
            bool: True if the user's actions are deleted, False otherwise.
        """
        actions_log_in_database = self._get_user_database_log(self.user_id)
        if actions_log_in_database.first():
            actions_log_in_database.delete()
            self.session.commit()
            self.session.flush()
            return True
        return False

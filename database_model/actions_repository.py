import logging
import os
import sys
from model.database_context import DatabaseContext
from model.table_actions import ActionsTable

logging.basicConfig(level=logging.DEBUG)

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class ActionsRepository:
    def __init__(self, user_id: str, type=None, cooperation=None, against=None) -> None:
        self.actions = {}
        self.action_id = ""
        self.user_id = user_id
        self.type = type
        self.cooperation = cooperation
        self.against = against
        database_context = DatabaseContext()
        database_context.initialize_database()
        self.session = database_context.session

    def _set_actions_data(self) -> None:
        self.actions["user_id"] = self.user_id
        self.actions["type"] = self.type
        self.actions["cooperation"] = self.cooperation
        self.actions["against"] = self.against
        self._check_data(self.actions)

    @staticmethod
    def _check_data(data) -> None:
        if not data["user_id"] or not data["type"]:
            logging.error("Data is missing.")
            sys.exit(1)

    def _get_user_database_log(self, user_id=None):
        logging.info(f"User id: {user_id}")
        if user_id is not None:
            query = self.session.query(ActionsTable).filter_by(user_id=user_id)
        else:
            query = self.session.query(ActionsTable).filter_by(
                user_id=self.user_id, type=self.type
            )
        return query

    def set_actions_data(self) -> None:
        self._set_actions_data()
        table = ActionsTable(**self.actions)
        logging.info("User data: %s", self.actions)
        actions_log_in_database = self._get_user_database_log()
        if actions_log_in_database.first() is not None:
            logging.info("User already exists in the database.")
            return actions_log_in_database.first()
        else:
            self.session.add(table)
            self.session.commit()
            self.session.flush()
            return table.id

    def get_user_actions_data(self) -> dict:
        actions_log_in_database = self._get_user_database_log(self.user_id)
        logging.info(f"User data: {actions_log_in_database.first()}")
        if actions_log_in_database.first() is not None:
            return actions_log_in_database
        return None

    def delete_all_user_actions(self) -> None:
        actions_log_in_database = self._get_user_database_log(self.user_id)
        if actions_log_in_database.first():
            actions_log_in_database.delete()
            self.session.commit()
            self.session.flush()
            return True
        return False

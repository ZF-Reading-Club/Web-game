import sys
import logging

from models.buildings import BuildingsTable
from models.database_context import DatabaseContext

logging.basicConfig(level=logging.DEBUG)


class BuildingsRepository:
    def __init__(
        self, type: str, price= ""|None, size= ""|None
    ) -> None:
        """
        Initializes a new instance of the buildings repository.
        Args:
            type (str): The type of the building.
            price (str, optional): The price of the building. Defaults to an empty string.
            size (str, optional): The size of the building. Defaults to an empty string.
        """

        self.data = {}
        self.user_id = ""
        self.type = type
        self.price = price
        self.size = size
        database_context = DatabaseContext()
        database_context.initialize_database()
        self.session = database_context.session

    @staticmethod
    def _set_building_data(self) -> None:
        """
        Sets test data for the instance.
        """

        self.data["type"] = self.type
        self.data["price"] = self.price
        self.data["size"] = self.size
        self._check_data(self.data)
        logging.info(self.data)

    @staticmethod
    def _check_data(data):
        """
        Checks if the data is valid.
        Args:
            data (dict): A dictionary containing user data.
        """
        if (
            not data["type"]
            or not data["price"]
            or not data["size"]
        ):
            logging.error("Data is missing.")
            sys.exit(1)

    @staticmethod
    def _get_building_database_log(self):
        """
        Retrieves the database log for the buildings with the specified type.

        Returns:
            sqlalchemy.orm.query.Query: A query object to fetch the buildings data from the UserTable.
        """

        query = self.session.query(BuildingsTable).filter_by(type=self.type)
        return query

    def set_building_data(self) -> None:
        """
        Adds the builing data to the database.
        """
        self._set_building_data()
        table = BuildingsTable(**self.data)
        building_in_database = self._get_building_database_log()

        if not building_in_database.first():
            self.session.add(table)
            self.session.flush()
            self.buil_id = table.id
            self.session.commit()
        else:
            logging.info(
                f"Building {self.type} is already in database with ID {building_in_database.first().id}."
            )

    def get_building_data(self) -> str | None:
        """
        Retrieves the building data from the database.
        """

        building_log = self._get_building_database_log().first()
        if not building_log:
            logging.info(f"User {self.type} is not in database")
            return None
        else:
            logging.info(
                f"Builiding {self.type} is in database with ID {building_log.id}"
            )
            building_id = building_log.id
            return building_id

    def delete_building(self):
        """
        Deletes the building from the database.
        """

        building_data = self._get_building_database_log()
        if building_data.first():
            logging.warning(
                f"Building {self.type} is going to be deleted from database."
                f"\n Data: {building_data.first().__dict__}"
            )
            building_data.delete()
            self.session.commit()
        else:
            logging.info(f"Building {self.type} is not in database")

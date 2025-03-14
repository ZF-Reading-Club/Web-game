import os
import sys
import logging

from model.table_user import UserTable
from model.database_context import DatabaseContext

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

logging.basicConfig(level=logging.DEBUG)

class AddDataToDatabase:
    def __init__(self, name, money, territory, buildings) -> None:
        """
        Initializes the instance with default values.
        Attributes:
            data (dict): A dictionary to store data.
            user_id (str): A string to store the user ID.
        """
        
        self.data = {}
        self.user_id = ""
        self.name = name
        self.money = money
        self.territory = territory
        self.buildings = buildings
        
       
    def set_test_data(self) -> None:
        """
        Sets test data for the instance.
        This method populates the `data` attribute with predefined test values:
        - name
        - money
        - territory
        - buildings
        """
        
        self.data["name"]= self.name  
        self.data["money"]= self.money
        self.data["territory"]= self.territory  
        self.data["buildings"]= self.buildings
        self._check_data(self.data)
        logging.info(self.data)
    
    def update_data(self, data) -> dict:
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
        if not data["name"] or not data["money"] or not data["territory"] or not data["buildings"]:
            sys.exit(1)
        if int(data["money"]) < 0:
            sys.exit(1)
        if int(data["territory"]) < 0:
            sys.exit(1)
        if int(data["buildings"]) < 0:
            sys.exit(1)

          
    def add_data_into_database(self) -> None:
        """
        Adds data into the database.
        This method initializes the database context, creates a session, and attempts to add a new user record.
        Attributes:
            self.data (dict): A dictionary containing user data to be added to the database.
            self.user_id (int): The ID of the user added to the database.
        Returns:
            None
        """
        
        database_context = DatabaseContext() 
        database_context.initialize_database()
        session = database_context.session
        
        table =  UserTable(**self.data)
        is_in_database = self.is_in_database(session)
        
        if not is_in_database.first():
            session.add(table)
            session.flush()
            self.user_id = table.id
            session.commit() 
        else:
            logging.info(f"User {self.data} is already in database with ID {is_in_database.first().id} and its status will be changed")
            data = is_in_database.first().__dict__
            data.pop('_sa_instance_state', None) 
            data = self.update_data(data)   
            session.query(UserTable).filter_by(id=is_in_database.first().id).update(data)
            session.flush()
            session.commit()
        
    def is_in_database(self, session):
        """
        Checks if the current data exists in the UserTable of the database.
        Args:
            session (Session): The SQLAlchemy session used to query the database.
        Returns:
            Query: The SQLAlchemy query object that can be used to check if the data exists in the database.
        """
        query = session.query(UserTable).filter_by(name=self.data["name"])
        return query    
    
    def main(self) -> None:
        self.set_test_data()
        self.add_data_into_database()
        
if __name__ == "__main__":
    AddDataToDatabase("Hoza", "10", "10", "10").main()
        
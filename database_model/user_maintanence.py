import os
import sys
import logging

from model.table_user import UserTable
from model.database_context import DatabaseContext

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

logging.basicConfig(level=logging.DEBUG)

class UserMaintanence:
    def __init__(self, name:str, money:str ="", territory:str="", buildings:str ="") -> None:
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
        
        self.data["name"]= self.name  
        self.data["money"]= self.money
        self.data["territory"]= self.territory  
        self.data["buildings"]= self.buildings
        self._check_data(self.data)
        logging.info(self.data)
    
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
        if not data["name"] or not data["money"] or not data["territory"] or not data["buildings"]:
            sys.exit(1)
        if int(data["money"]) < 0:
            sys.exit(1)
        if int(data["territory"]) < 0:
            sys.exit(1)
        if int(data["buildings"]) < 0:
            sys.exit(1)

    @staticmethod    
    def _get_user_database_log(self):
        
        query = self.session.query(UserTable).filter_by(name=self.name)
        return query
          
    def upser_user_data(self) -> None:
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
        table =  UserTable(**self.data)
        user_in_database = self._get_user_database_log()
        
        if not user_in_database.first():
            self.session.add(table)
            self.session.flush()
            self.user_id = table.id
            self.session.commit() 
        else:
            logging.info(f"User {self.data} is already in database with ID {user_in_database.first().id} and its status will be changed")
            data = user_in_database.first().__dict__
            data.pop('_sa_instance_state', None) 
            data = self.update_data(data)   
            self.session.query(UserTable).filter_by(id=user_in_database.first().id).update(data)
            self.session.flush()
            self.session.commit()
        
    def get_user_data(self):
        user_log = self._get_user_database_log().first()
        if not user_log:
            logging.info(f"User {self.name} is not in database")
            return None
        else:
            logging.info(f"User {self.name} is already in database with ID {user_log.id}.")
            data = user_log.__dict__
            data.pop('_sa_instance_state', None) 
            return data


    def delete_user(self):
        user_data = self._get_user_database_log()
        if user_data.first():
            logging.warning(f"User {self.name} is going to be deleted from database." 
                            f"\n Data: {user_data.first().__dict__}")
            user_data.delete()
            self.session.commit()
        else: 
            logging.info(f"User {self.name} is not in database")
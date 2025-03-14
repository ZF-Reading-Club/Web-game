import os
import sys

from model.table_user import UserTable
from model.database_context import DatabaseContext

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class AddDataTest:
    def __init__(self) -> None:
        """
        Initializes the instance with default values.
        Attributes:
            data (dict): A dictionary to store data.
            user_id (str): A string to store the user ID.
        """
        
        self.data = {}
        self.user_id = ""
       
    def set_test_data(self):
        """
        Sets test data for the instance.
        This method populates the `data` attribute with predefined test values:
        - name
        - money
        - territory
        - buildings
        """
        
        self.data["name"]="Hoa"    
        self.data["money"]="123"    
        self.data["territory"]="none"   
        self.data["buildings"]="shelter"
        print(self.data)
        
    def add_data_into_database(self):
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
        #print(is_in_database)
        
        if not is_in_database.first():
            session.add(table)
            session.flush()
            self.user_id = table.id
            session.commit() 
        else:
            print(is_in_database.first().id)    
        
    def is_in_database(self, session):
        """
        Checks if the current data exists in the UserTable of the database.
        Args:
            session (Session): The SQLAlchemy session used to query the database.
        Returns:
            Query: The SQLAlchemy query object that can be used to check if the data exists in the database.
        """
        query = session.query(UserTable).filter_by(**self.data)
        return query    
    
    def main(self):
        self.set_test_data()
        self.add_data_into_database()
        
if __name__ == "__main__":
    AddDataTest().main()
        
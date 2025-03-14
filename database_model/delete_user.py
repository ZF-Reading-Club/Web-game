import sys
import os
import logging

from model.table_user import UserTable
from model.database_context import DatabaseContext

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
logging.basicConfig(level=logging.DEBUG)

class DeleteUser():
    
    def __init__(self, name):
        database_context = DatabaseContext() 
        database_context.initialize_database()
        self.session = database_context.session
        self.name = name

    def get_user_database_log(self):
        query = self.session.query(UserTable).filter_by(name=self.name)
        return query

    def delete_user(self):
        user_data = self.get_user_database_log()
        if user_data.first():
            logging.warning(f"User {self.name} is going to be deleted from database." 
                            f"\n Data: {user_data.first().__dict__}")
            user_data.delete()
            self.session.commit()
        else: 
            logging.info(f"User {self.name} is not in database")

        
if __name__ == "__main__":
    DeleteUser("Hoza").delete_user()
  
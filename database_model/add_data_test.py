import os
import sys

from model.table_user import UserTable
from model.database_context import DatabaseContext

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class AddDataTest:
    def __init__(self) -> None:
        self.data = {}
        self.user_id = ""
       
    def set_test_data(self):
        self.data["name"]="Kamila"    
        self.data["money"]="123"    
        self.data["territory"]="all"   
        self.data["buildings"]="lots"
        print(self.data)
        
    def add_data_into_database(self):
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
        
    def is_in_database(self, session):
        query = session.query(UserTable).first_by(**self.data)
        return query    
    
    def main(self):
        self.set_test_data()
        self.add_data_into_database()
        
if __name__ == "__main__":
    AddDataTest().main()
        
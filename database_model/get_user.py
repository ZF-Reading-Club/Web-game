from model.table_user import UserTable
from model.database_context import DatabaseContext

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
logging.basicConfig(level=logging.DEBUG)

class GetUser():
    def __init__(self, name):
        self.name = name

    def get_user_database_log(self):
        database_context = DatabaseContext() 
        database_context.initialize_database()
        session = database_context.session
        query = session.query(UserTable).filter_by(name=self.name)
        return query
        
    def get_user_data(self):
        user_log = self.get_user_database_log().first()
        if not user_log:
            logging.info(f"User {self.name} is not in database")
            return None
        else:
            logging.info(f"User {self.name} is already in database with ID {is_in_database.first().id}.")
            data = is_in_database.first().__dict__
            data.pop('_sa_instance_state', None) 
            return data

        
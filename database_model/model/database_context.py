import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class DatabaseContext:
    HOST= "127.0.0.1:5432" #have to change
    DATABASE = "web_game"
    USER = "admin"
    PASSWORD = "admin"
    
    Base = declarative_base()
    
    def __init__(self) -> None:
        """Initialize database connection."""
        url=f'postgresql://{self.USER}:{self.PASSWORD}@{self.HOST}/{self.DATABASE}'
        self.engine = create_engine(url)
        Session = sessionmaker(bind=self.engine)
        self.session=Session()
        
    def initialize_database(self):
        self.Base.metadata.create_all(self.engine)
        
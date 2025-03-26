from sqlalchemy import Column, Integer, String  
from .database_context import DatabaseContext  
  
  
class BuildingsTable(DatabaseContext.Base):  
    __tablename__ = "buildings"  
    id = Column(Integer, primary_key=True, nullable=True, autoincrement=True)  
    type = Column(String)  
    price = Column(String)  
    size = Column(String)  
    
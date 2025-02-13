from sqlalchemy import Column, Integer, String  
from .database_context import DatabaseContext  
  
  
class ComponentsTable(DatabaseContext.Base):  
    __tablename__ = "user"  
    id = Column(Integer, primary_key=True, nullable=True, autoincrement=True)  
    name = Column(String)  
    money = Column(String)  
    territory = Column(String)  
    buildings = Column(String)
from sqlalchemy import Column, Integer, String  
from .database_context import DatabaseContext  
  
  
class ActionsTable(DatabaseContext.Base):  
    __tablename__ = "actions"  
    id = Column(Integer, primary_key=True, nullable=True, autoincrement=True)  
    user_id = Column(Integer)  #link to previous table
    type = Column(String)  
    cooperation = Column(String)  
    against = Column(String)  
    
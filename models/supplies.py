from sqlalchemy import Column,Integer,String,Float

from config.database import Base

class Supplies(Base): 
    
    __tablename__ = "supplies"
    
    id = Column(Integer,primary_key=True)
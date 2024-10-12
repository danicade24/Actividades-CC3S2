#from ..db.database import Base
from src.db.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY

class Question(Base):
    __tablename__ = "questions"
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    description = Column(String, nullable=False)
    options = Column(ARRAY(String), nullable=False)
    correct_answer = Column(String, nullable=False)
    level = Column(String, nullable=False)
from pydantic import BaseModel
from typing import List

class QuestionBase(BaseModel):
    description: str
    options: List[str]
    correct_answer: str
    level: str
    
    class Config:
        orm_mode = True
        # Habilita from_attributes
        from_attributes = True

class QuestionRequest(QuestionBase):
    class Config:
        orm_mode = True
        from_attributes = True

class QuestionResponse(QuestionBase):
    id: int
    
    class Config:
        orm_mode = True
        from_attributes = True

from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field


class RecommendationCreate(BaseModel):
    user_id:UUID
    problem_id:UUID
    reason:str
    score:float=Field(ge=0.0)
    status:str="pending"



class RecommendationResponse(BaseModel):
    id:UUID
    user_id:UUID
    problem_id:UUID
    score:float
    reason:str
    status:str
    created_at:datetime


    model_config=ConfigDict(from_attributes=True)
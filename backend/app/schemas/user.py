from datetime import datetime 
from uuid import UUID
from pydantic import BaseModel, ConfigDict, EmailStr

class UserCreate(BaseModel):
    username:str
    email:EmailStr
    password:str



class UserResponse(BaseModel):
    id:UUID
    username:str
    email:EmailStr
    created_at:datetime
    updated_at:datetime


    model_config=ConfigDict(from_attributes=True)
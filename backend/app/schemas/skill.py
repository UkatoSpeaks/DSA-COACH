from uuid import UUID
from pydantic import BaseModel, ConfigDict


class SkillCreate(BaseModel):
    name:str
    description:str|None=None



class SkillResponse(BaseModel):
    id:UUID
    name:str
    description:str|None


    model_config=ConfigDict(from_attributes=True)
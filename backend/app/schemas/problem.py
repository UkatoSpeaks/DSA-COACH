from uuid  import UUID
from pydantic import BaseModel, ConfigDict

class ProblemCreate(BaseModel):
    title:str
    description:str
    difficulty:str
    leetcode_url:str|None=None
    tags:str|None=None


class ProblemResponse(BaseModel):
    id:UUID
    title:str
    description:str
    difficulty:str
    leetcode_url:str|None
    tags:str|None


    model_config=ConfigDict(from_attributes=True)
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field


class UserSkillCreate(BaseModel):
    user_id:UUID
    skill_id:UUID
    proficiency:float=Field(default=0.0, ge=0.0, le=100.0)



class UserSkillResponse(BaseModel):
    id:UUID
    user_id:UUID
    skill_id:UUID
    proficiency:float

    model_config=ConfigDict(from_attributes=True)
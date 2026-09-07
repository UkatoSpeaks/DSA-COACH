from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class LearningSessionCreate(BaseModel):
    user_id: UUID
    current_skill_id: UUID | None = None


class LearningSessionResponse(BaseModel):
    id: UUID
    user_id: UUID
    current_skill_id: UUID | None
    status: str
    started_at: datetime
    ended_at: datetime | None

    model_config = ConfigDict(from_attributes=True)
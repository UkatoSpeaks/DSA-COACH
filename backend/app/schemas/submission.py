from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class SubmissionCreate(BaseModel):
    user_id: UUID
    problem_id: UUID
    code: str
    language: str
    status: str
    runtime_ms: int | None = None
    memory_kb: int | None = None


class SubmissionResponse(BaseModel):
    id: UUID
    user_id: UUID
    problem_id: UUID
    code: str
    language: str
    status: str
    runtime_ms: int | None
    memory_kb: int | None
    submitted_at: datetime

    model_config = ConfigDict(from_attributes=True)
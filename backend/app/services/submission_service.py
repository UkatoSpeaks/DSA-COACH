from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.submission import Submission
from app.repositories.submission_repository import SubmissionRepository
from app.schemas.submission import SubmissionCreate


class SubmissionService:

    @staticmethod
    async def create_submission(
        db: AsyncSession,
        data: SubmissionCreate,
    ) -> Submission:

        submission = Submission(
            user_id=data.user_id,
            problem_id=data.problem_id,
            code=data.code,
            language=data.language,
            status=data.status,
            runtime_ms=data.runtime_ms,
            memory_kb=data.memory_kb,
        )

        return await SubmissionRepository.create(
            db,
            submission,
        )

    @staticmethod
    async def get_submission(
        db: AsyncSession,
        submission_id: UUID,
    ) -> Submission | None:

        return await SubmissionRepository.get_by_id(
            db,
            submission_id,
        )

    @staticmethod
    async def get_user_submissions(
        db: AsyncSession,
        user_id: UUID,
    ) -> list[Submission]:

        return await SubmissionRepository.get_by_user(
            db,
            user_id,
        )

    @staticmethod
    async def get_problem_submissions(
        db: AsyncSession,
        problem_id: UUID,
    ) -> list[Submission]:

        return await SubmissionRepository.get_by_problem(
            db,
            problem_id,
        )
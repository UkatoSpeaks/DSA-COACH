from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.submission import Submission


class SubmissionRepository:

    @staticmethod
    async def create(
        db: AsyncSession,
        submission: Submission,
    ) -> Submission:
        db.add(submission)
        await db.commit()
        await db.refresh(submission)

        return submission

    @staticmethod
    async def get_by_id(
        db: AsyncSession,
        submission_id: UUID,
    ) -> Submission | None:
        result = await db.execute(
            select(Submission).where(
                Submission.id == submission_id
            )
        )

        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_user(
        db: AsyncSession,
        user_id: UUID,
    ) -> list[Submission]:
        result = await db.execute(
            select(Submission)
            .where(Submission.user_id == user_id)
            .order_by(Submission.submitted_at.desc())
        )

        return list(result.scalars().all())

    @staticmethod
    async def get_by_problem(
        db: AsyncSession,
        problem_id: UUID,
    ) -> list[Submission]:
        result = await db.execute(
            select(Submission)
            .where(Submission.problem_id == problem_id)
            .order_by(Submission.submitted_at.desc())
        )

        return list(result.scalars().all())
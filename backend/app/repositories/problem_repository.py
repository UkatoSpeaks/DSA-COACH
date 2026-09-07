from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.problem import Problem


class ProblemRepository:

    @staticmethod
    async def create(
        db: AsyncSession,
        problem: Problem,
    ) -> Problem:
        db.add(problem)
        await db.commit()
        await db.refresh(problem)

        return problem

    @staticmethod
    async def get_by_id(
        db: AsyncSession,
        problem_id: UUID,
    ) -> Problem | None:
        result = await db.execute(
            select(Problem).where(Problem.id == problem_id)
        )

        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_difficulty(
        db: AsyncSession,
        difficulty: str,
    ) -> list[Problem]:
        result = await db.execute(
            select(Problem)
            .where(Problem.difficulty == difficulty)
        )

        return list(result.scalars().all())

    @staticmethod
    async def get_all(
        db: AsyncSession,
    ) -> list[Problem]:
        result = await db.execute(
            select(Problem)
        )

        return list(result.scalars().all())

    @staticmethod
    async def delete(
        db: AsyncSession,
        problem: Problem,
    ) -> None:
        await db.delete(problem)
        await db.commit()
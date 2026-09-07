from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.problem import Problem
from app.repositories.problem_repository import ProblemRepository
from app.schemas.problem import ProblemCreate


class ProblemService:

    @staticmethod
    async def create_problem(
        db: AsyncSession,
        data: ProblemCreate,
    ) -> Problem:

        problem = Problem(
            title=data.title,
            description=data.description,
            difficulty=data.difficulty,
            leetcode_url=data.leetcode_url,
            tags=data.tags,
        )

        return await ProblemRepository.create(
            db,
            problem,
        )

    @staticmethod
    async def get_problem(
        db: AsyncSession,
        problem_id: UUID,
    ) -> Problem | None:

        return await ProblemRepository.get_by_id(
            db,
            problem_id,
        )

    @staticmethod
    async def get_all_problems(
        db: AsyncSession,
    ) -> list[Problem]:

        return await ProblemRepository.get_all(
            db,
        )

    @staticmethod
    async def get_problems_by_difficulty(
        db: AsyncSession,
        difficulty: str,
    ) -> list[Problem]:

        return await ProblemRepository.get_by_difficulty(
            db,
            difficulty,
        )

    @staticmethod
    async def delete_problem(
        db: AsyncSession,
        problem_id: UUID,
    ) -> bool:

        problem = await ProblemRepository.get_by_id(
            db,
            problem_id,
        )

        if not problem:
            return False

        await ProblemRepository.delete(
            db,
            problem,
        )

        return True
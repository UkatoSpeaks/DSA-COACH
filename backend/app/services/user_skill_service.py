from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user_skill import UserSkill
from app.repositories.user_skill_repository import UserSkillRepository
from app.schemas.user_skill import UserSkillCreate


class UserSkillService:

    @staticmethod
    async def create_user_skill(
        db: AsyncSession,
        data: UserSkillCreate,
    ) -> UserSkill:

        existing = await UserSkillRepository.get_by_user_and_skill(
            db,
            data.user_id,
            data.skill_id,
        )

        if existing:
            raise ValueError(
                "User skill already exists"
            )

        user_skill = UserSkill(
            user_id=data.user_id,
            skill_id=data.skill_id,
            proficiency=data.proficiency,
        )

        return await UserSkillRepository.create(
            db,
            user_skill,
        )

    @staticmethod
    async def get_user_skill(
        db: AsyncSession,
        user_skill_id: UUID,
    ) -> UserSkill | None:

        return await UserSkillRepository.get_by_id(
            db,
            user_skill_id,
        )

    @staticmethod
    async def get_user_skills(
        db: AsyncSession,
        user_id: UUID,
    ) -> list[UserSkill]:

        return await UserSkillRepository.get_by_user(
            db,
            user_id,
        )

    @staticmethod
    async def get_user_skill_by_skill(
        db: AsyncSession,
        user_id: UUID,
        skill_id: UUID,
    ) -> UserSkill | None:

        return await UserSkillRepository.get_by_user_and_skill(
            db,
            user_id,
            skill_id,
        )

    @staticmethod
    async def update_proficiency(
        db: AsyncSession,
        user_id: UUID,
        skill_id: UUID,
        proficiency: float,
    ) -> UserSkill | None:

        user_skill = await UserSkillRepository.get_by_user_and_skill(
            db,
            user_id,
            skill_id,
        )

        if not user_skill:
            return None

        if proficiency < 0 or proficiency > 100:
            raise ValueError(
                "Proficiency must be between 0 and 100"
            )

        return await UserSkillRepository.update_proficiency(
            db,
            user_skill,
            proficiency,
        )
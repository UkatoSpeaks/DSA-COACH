from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.skill import Skill
from app.repositories.skill_repository import SkillRepository
from app.schemas.skill import SkillCreate


class SkillService:

    @staticmethod
    async def create_skill(
        db: AsyncSession,
        data: SkillCreate,
    ) -> Skill:

        existing_skill = await SkillRepository.get_by_name(
            db,
            data.name,
        )

        if existing_skill:
            raise ValueError("Skill already exists")

        skill = Skill(
            name=data.name,
            description=data.description,
        )

        return await SkillRepository.create(
            db,
            skill,
        )

    @staticmethod
    async def get_skill(
        db: AsyncSession,
        skill_id: UUID,
    ) -> Skill | None:

        return await SkillRepository.get_by_id(
            db,
            skill_id,
        )

    @staticmethod
    async def get_skill_by_name(
        db: AsyncSession,
        name: str,
    ) -> Skill | None:

        return await SkillRepository.get_by_name(
            db,
            name,
        )

    @staticmethod
    async def get_all_skills(
        db: AsyncSession,
    ) -> list[Skill]:

        return await SkillRepository.get_all(
            db,
        )

    @staticmethod
    async def delete_skill(
        db: AsyncSession,
        skill_id: UUID,
    ) -> bool:

        skill = await SkillRepository.get_by_id(
            db,
            skill_id,
        )

        if not skill:
            return False

        await SkillRepository.delete(
            db,
            skill,
        )

        return True
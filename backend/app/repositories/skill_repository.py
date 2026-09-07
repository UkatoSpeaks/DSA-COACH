from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.skill import Skill


class SkillRepository:

    @staticmethod
    async def create(
        db: AsyncSession,
        skill: Skill,
    ) -> Skill:
        db.add(skill)
        await db.commit()
        await db.refresh(skill)

        return skill

    @staticmethod
    async def get_by_id(
        db: AsyncSession,
        skill_id: UUID,
    ) -> Skill | None:
        result = await db.execute(
            select(Skill).where(Skill.id == skill_id)
        )

        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_name(
        db: AsyncSession,
        name: str,
    ) -> Skill | None:
        result = await db.execute(
            select(Skill).where(Skill.name == name)
        )

        return result.scalar_one_or_none()

    @staticmethod
    async def get_all(
        db: AsyncSession,
    ) -> list[Skill]:
        result = await db.execute(
            select(Skill).order_by(Skill.name)
        )

        return list(result.scalars().all())

    @staticmethod
    async def delete(
        db: AsyncSession,
        skill: Skill,
    ) -> None:
        await db.delete(skill)
        await db.commit()
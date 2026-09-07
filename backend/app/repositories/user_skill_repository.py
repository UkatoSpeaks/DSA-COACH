from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user_skill import UserSkill


class UserSkillRepository:

    @staticmethod
    async def create(
        db: AsyncSession,
        user_skill: UserSkill,
    ) -> UserSkill:
        db.add(user_skill)
        await db.commit()
        await db.refresh(user_skill)

        return user_skill

    @staticmethod
    async def get_by_id(
        db: AsyncSession,
        user_skill_id: UUID,
    ) -> UserSkill | None:
        result = await db.execute(
            select(UserSkill).where(
                UserSkill.id == user_skill_id
            )
        )

        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_user(
        db: AsyncSession,
        user_id: UUID,
    ) -> list[UserSkill]:
        result = await db.execute(
            select(UserSkill).where(
                UserSkill.user_id == user_id
            )
        )

        return list(result.scalars().all())

    @staticmethod
    async def get_by_user_and_skill(
        db: AsyncSession,
        user_id: UUID,
        skill_id: UUID,
    ) -> UserSkill | None:
        result = await db.execute(
            select(UserSkill).where(
                UserSkill.user_id == user_id,
                UserSkill.skill_id == skill_id,
            )
        )

        return result.scalar_one_or_none()

    @staticmethod
    async def update_proficiency(
        db: AsyncSession,
        user_skill: UserSkill,
        proficiency: float,
    ) -> UserSkill:
        user_skill.proficiency = proficiency

        await db.commit()
        await db.refresh(user_skill)

        return user_skill
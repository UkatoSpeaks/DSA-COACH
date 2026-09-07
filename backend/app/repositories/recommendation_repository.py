from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.recommendation import Recommendation


class RecommendationRepository:

    @staticmethod
    async def create(
        db: AsyncSession,
        recommendation: Recommendation,
    ) -> Recommendation:
        db.add(recommendation)
        await db.commit()
        await db.refresh(recommendation)

        return recommendation

    @staticmethod
    async def get_by_id(
        db: AsyncSession,
        recommendation_id: UUID,
    ) -> Recommendation | None:
        result = await db.execute(
            select(Recommendation).where(
                Recommendation.id == recommendation_id
            )
        )

        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_user(
        db: AsyncSession,
        user_id: UUID,
    ) -> list[Recommendation]:
        result = await db.execute(
            select(Recommendation)
            .where(Recommendation.user_id == user_id)
            .order_by(Recommendation.created_at.desc())
        )

        return list(result.scalars().all())

    @staticmethod
    async def get_pending_by_user(
        db: AsyncSession,
        user_id: UUID,
    ) -> list[Recommendation]:
        result = await db.execute(
            select(Recommendation)
            .where(
                Recommendation.user_id == user_id,
                Recommendation.status == "pending",
            )
            .order_by(Recommendation.score.desc())
        )

        return list(result.scalars().all())

    @staticmethod
    async def update_status(
        db: AsyncSession,
        recommendation: Recommendation,
        status: str,
    ) -> Recommendation:
        recommendation.status = status

        await db.commit()
        await db.refresh(recommendation)

        return recommendation
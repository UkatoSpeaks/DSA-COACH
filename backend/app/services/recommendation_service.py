from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.recommendation import Recommendation
from app.repositories.recommendation_repository import (
    RecommendationRepository,
)
from app.schemas.recommendation import RecommendationCreate


class RecommendationService:

    @staticmethod
    async def create_recommendation(
        db: AsyncSession,
        data: RecommendationCreate,
    ) -> Recommendation:

        recommendation = Recommendation(
            user_id=data.user_id,
            problem_id=data.problem_id,
            reason=data.reason,
            score=data.score,
            status=data.status,
        )

        return await RecommendationRepository.create(
            db,
            recommendation,
        )

    @staticmethod
    async def get_recommendation(
        db: AsyncSession,
        recommendation_id: UUID,
    ) -> Recommendation | None:

        return await RecommendationRepository.get_by_id(
            db,
            recommendation_id,
        )

    @staticmethod
    async def get_user_recommendations(
        db: AsyncSession,
        user_id: UUID,
    ) -> list[Recommendation]:

        return await RecommendationRepository.get_by_user(
            db,
            user_id,
        )

    @staticmethod
    async def get_pending_recommendations(
        db: AsyncSession,
        user_id: UUID,
    ) -> list[Recommendation]:

        return await RecommendationRepository.get_pending_by_user(
            db,
            user_id,
        )

    @staticmethod
    async def update_status(
        db: AsyncSession,
        recommendation_id: UUID,
        status: str,
    ) -> Recommendation | None:

        recommendation = await RecommendationRepository.get_by_id(
            db,
            recommendation_id,
        )

        if not recommendation:
            return None

        return await RecommendationRepository.update_status(
            db,
            recommendation,
            status,
        )
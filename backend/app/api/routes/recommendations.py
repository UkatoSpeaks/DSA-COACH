from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.schemas.recommendation import (
    RecommendationCreate,
    RecommendationResponse,
)
from app.services.recommendation_service import (
    RecommendationService,
)


router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"],
)


@router.post(
    "/",
    response_model=RecommendationResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_recommendation(
    data: RecommendationCreate,
    db: AsyncSession = Depends(get_db),
):
    return await RecommendationService.create_recommendation(
        db,
        data,
    )


@router.get(
    "/{recommendation_id}",
    response_model=RecommendationResponse,
)
async def get_recommendation(
    recommendation_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    recommendation = await RecommendationService.get_recommendation(
        db,
        recommendation_id,
    )

    if not recommendation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recommendation not found",
        )

    return recommendation


@router.get(
    "/user/{user_id}",
    response_model=list[RecommendationResponse],
)
async def get_user_recommendations(
    user_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    return await RecommendationService.get_user_recommendations(
        db,
        user_id,
    )


@router.get(
    "/user/{user_id}/pending",
    response_model=list[RecommendationResponse],
)
async def get_pending_recommendations(
    user_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    return await RecommendationService.get_pending_recommendations(
        db,
        user_id,
    )


@router.patch(
    "/{recommendation_id}/status",
    response_model=RecommendationResponse,
)
async def update_recommendation_status(
    recommendation_id: UUID,
    status_value: str,
    db: AsyncSession = Depends(get_db),
):
    recommendation = await RecommendationService.update_status(
        db,
        recommendation_id,
        status_value,
    )

    if not recommendation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recommendation not found",
        )

    return recommendation
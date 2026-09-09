from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.schemas.user_skill import (
    UserSkillCreate,
    UserSkillResponse,
)
from app.services.user_skill_service import UserSkillService


router = APIRouter(
    prefix="/user-skills",
    tags=["User Skills"],
)


@router.post(
    "/",
    response_model=UserSkillResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_user_skill(
    data: UserSkillCreate,
    db: AsyncSession = Depends(get_db),
):
    try:
        return await UserSkillService.create_user_skill(
            db,
            data,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.get(
    "/user/{user_id}",
    response_model=list[UserSkillResponse],
)
async def get_user_skills(
    user_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    return await UserSkillService.get_user_skills(
        db,
        user_id,
    )


@router.get(
    "/{user_skill_id}",
    response_model=UserSkillResponse,
)
async def get_user_skill(
    user_skill_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    user_skill = await UserSkillService.get_user_skill(
        db,
        user_skill_id,
    )

    if not user_skill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User skill not found",
        )

    return user_skill


@router.patch(
    "/user/{user_id}/skill/{skill_id}",
    response_model=UserSkillResponse,
)
async def update_proficiency(
    user_id: UUID,
    skill_id: UUID,
    proficiency: float,
    db: AsyncSession = Depends(get_db),
):
    user_skill = await UserSkillService.update_proficiency(
        db,
        user_id,
        skill_id,
        proficiency,
    )

    if not user_skill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User skill not found",
        )

    return user_skill
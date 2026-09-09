from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.schemas.skill import SkillCreate, SkillResponse
from app.services.skill_service import SkillService


router = APIRouter(
    prefix="/skills",
    tags=["Skills"],
)


@router.post(
    "/",
    response_model=SkillResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_skill(
    data: SkillCreate,
    db: AsyncSession = Depends(get_db),
):
    try:
        return await SkillService.create_skill(
            db,
            data,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.get(
    "/",
    response_model=list[SkillResponse],
)
async def get_all_skills(
    db: AsyncSession = Depends(get_db),
):
    return await SkillService.get_all_skills(
        db,
    )


@router.get(
    "/{skill_id}",
    response_model=SkillResponse,
)
async def get_skill(
    skill_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    skill = await SkillService.get_skill(
        db,
        skill_id,
    )

    if not skill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Skill not found",
        )

    return skill
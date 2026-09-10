from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.schemas.learning_session import (
    LearningSessionCreate,
    LearningSessionResponse,
)
from app.services.learning_session_service import (
    LearningSessionService,
)


router = APIRouter(
    prefix="/learning-sessions",
    tags=["Learning Sessions"],
)


@router.post(
    "/",
    response_model=LearningSessionResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_session(
    data: LearningSessionCreate,
    db: AsyncSession = Depends(get_db),
):
    try:
        return await LearningSessionService.create_session(
            db,
            data,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.get(
    "/{session_id}",
    response_model=LearningSessionResponse,
)
async def get_session(
    session_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    session = await LearningSessionService.get_session(
        db,
        session_id,
    )

    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Learning session not found",
        )

    return session


@router.get(
    "/user/{user_id}/active",
    response_model=LearningSessionResponse | None,
)
async def get_active_session(
    user_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    return await LearningSessionService.get_active_session(
        db,
        user_id,
    )


@router.get(
    "/user/{user_id}",
    response_model=list[LearningSessionResponse],
)
async def get_user_sessions(
    user_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    return await LearningSessionService.get_user_sessions(
        db,
        user_id,
    )


@router.patch(
    "/{session_id}/end",
    response_model=LearningSessionResponse,
)
async def end_session(
    session_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    session = await LearningSessionService.end_session(
        db,
        session_id,
    )

    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Learning session not found",
        )

    return session
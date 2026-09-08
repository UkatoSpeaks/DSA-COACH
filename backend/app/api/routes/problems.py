from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.schemas.problem import ProblemCreate, ProblemResponse
from app.services.problem_service import ProblemService


router = APIRouter(
    prefix="/problems",
    tags=["Problems"],
)


@router.post(
    "/",
    response_model=ProblemResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_problem(
    data: ProblemCreate,
    db: AsyncSession = Depends(get_db),
):
    return await ProblemService.create_problem(
        db,
        data,
    )


@router.get(
    "/",
    response_model=list[ProblemResponse],
)
async def get_all_problems(
    db: AsyncSession = Depends(get_db),
):
    return await ProblemService.get_all_problems(
        db,
    )


@router.get(
    "/{problem_id}",
    response_model=ProblemResponse,
)
async def get_problem(
    problem_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    problem = await ProblemService.get_problem(
        db,
        problem_id,
    )

    if not problem:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Problem not found",
        )

    return problem


@router.get(
    "/difficulty/{difficulty}",
    response_model=list[ProblemResponse],
)
async def get_problems_by_difficulty(
    difficulty: str,
    db: AsyncSession = Depends(get_db),
):
    return await ProblemService.get_problems_by_difficulty(
        db,
        difficulty,
    )


@router.delete(
    "/{problem_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_problem(
    problem_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    deleted = await ProblemService.delete_problem(
        db,
        problem_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Problem not found",
        )
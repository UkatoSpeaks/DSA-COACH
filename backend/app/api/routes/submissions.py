from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.schemas.submission import (
    SubmissionCreate,
    SubmissionResponse,
    SubmissionAnalysisResponse,
)
from app.services.submission_service import SubmissionService
from app.services.ai_service import AIService
from app.services.problem_service import ProblemService


router = APIRouter(
    prefix="/submissions",
    tags=["Submissions"],
)


@router.post(
    "/",
    response_model=SubmissionAnalysisResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_submission(
    data: SubmissionCreate,
    db: AsyncSession = Depends(get_db),
):
    submission = await SubmissionService.create_submission(
        db,
        data,
    )

    problem = await ProblemService.get_problem(
        db,
        data.problem_id,
    )

    if not problem:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Problem not found",
        )

    analysis = await AIService.analyze_submission(
        problem=problem.description,
        code=data.code,
        language=data.language,
    )

    return SubmissionAnalysisResponse(
        submission=submission,
        analysis=analysis,
    )


@router.get(
    "/{submission_id}",
    response_model=SubmissionResponse,
)
async def get_submission(
    submission_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    submission = await SubmissionService.get_submission(
        db,
        submission_id,
    )

    if not submission:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Submission not found",
        )

    return submission


@router.get(
    "/user/{user_id}",
    response_model=list[SubmissionResponse],
)
async def get_user_submissions(
    user_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    return await SubmissionService.get_user_submissions(
        db,
        user_id,
    )


@router.get(
    "/problem/{problem_id}",
    response_model=list[SubmissionResponse],
)
async def get_problem_submissions(
    problem_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    return await SubmissionService.get_problem_submissions(
        db,
        problem_id,
    )

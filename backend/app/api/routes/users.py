from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    data: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    try:
        return await UserService.create_user(
            db,
            data,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.get(
    "/{user_id}",
    response_model=UserResponse,
)
async def get_user(
    user_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    user = await UserService.get_user(
        db,
        user_id,
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user
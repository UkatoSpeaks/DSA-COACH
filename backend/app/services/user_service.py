from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


class UserService:

    @staticmethod
    async def create_user(
        db: AsyncSession,
        data: UserCreate,
    ) -> User:

        existing_email = await UserRepository.get_by_email(
            db,
            data.email,
        )

        if existing_email:
            raise ValueError("Email already registered")

        existing_username = await UserRepository.get_by_username(
            db,
            data.username,
        )

        if existing_username:
            raise ValueError("Username already registered")

        user = User(
            username=data.username,
            email=data.email,
            hashed_password=data.password,
        )

        return await UserRepository.create(
            db,
            user,
        )

    @staticmethod
    async def get_user(
        db: AsyncSession,
        user_id,
    ) -> User | None:

        return await UserRepository.get_by_id(
            db,
            user_id,
        )

    @staticmethod
    async def get_user_by_email(
        db: AsyncSession,
        email: str,
    ) -> User | None:

        return await UserRepository.get_by_email(
            db,
            email,
        )
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.learning_session import LearningSession
from app.repositories.learning_session_repository import (
    LearningSessionRepository,
)
from app.schemas.learning_session import LearningSessionCreate


class LearningSessionService:

    @staticmethod
    async def create_session(
        db: AsyncSession,
        data: LearningSessionCreate,
    ) -> LearningSession:

        active_session = (
            await LearningSessionRepository.get_active_by_user(
                db,
                data.user_id,
            )
        )

        if active_session:
            raise ValueError(
                "User already has an active learning session"
            )

        session = LearningSession(
            user_id=data.user_id,
            current_skill_id=data.current_skill_id,
            status="active",
        )

        return await LearningSessionRepository.create(
            db,
            session,
        )

    @staticmethod
    async def get_session(
        db: AsyncSession,
        session_id: UUID,
    ) -> LearningSession | None:

        return await LearningSessionRepository.get_by_id(
            db,
            session_id,
        )

    @staticmethod
    async def get_active_session(
        db: AsyncSession,
        user_id: UUID,
    ) -> LearningSession | None:

        return await LearningSessionRepository.get_active_by_user(
            db,
            user_id,
        )

    @staticmethod
    async def get_user_sessions(
        db: AsyncSession,
        user_id: UUID,
    ) -> list[LearningSession]:

        return await LearningSessionRepository.get_by_user(
            db,
            user_id,
        )

    @staticmethod
    async def end_session(
        db: AsyncSession,
        session_id: UUID,
    ) -> LearningSession | None:

        session = await LearningSessionRepository.get_by_id(
            db,
            session_id,
        )

        if not session:
            return None

        if session.status == "completed":
            return session

        return await LearningSessionRepository.end_session(
            db,
            session,
        )
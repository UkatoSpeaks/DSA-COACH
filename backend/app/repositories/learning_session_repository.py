from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.learning_session import LearningSession


class LearningSessionRepository:

    @staticmethod
    async def create(
        db: AsyncSession,
        session: LearningSession,
    ) -> LearningSession:
        db.add(session)
        await db.commit()
        await db.refresh(session)

        return session

    @staticmethod
    async def get_by_id(
        db: AsyncSession,
        session_id: UUID,
    ) -> LearningSession | None:
        result = await db.execute(
            select(LearningSession).where(
                LearningSession.id == session_id
            )
        )

        return result.scalar_one_or_none()

    @staticmethod
    async def get_active_by_user(
        db: AsyncSession,
        user_id: UUID,
    ) -> LearningSession | None:
        result = await db.execute(
            select(LearningSession)
            .where(
                LearningSession.user_id == user_id,
                LearningSession.status == "active",
            )
            .order_by(LearningSession.started_at.desc())
        )

        return result.scalars().first()

    @staticmethod
    async def get_by_user(
        db: AsyncSession,
        user_id: UUID,
    ) -> list[LearningSession]:
        result = await db.execute(
            select(LearningSession)
            .where(LearningSession.user_id == user_id)
            .order_by(LearningSession.started_at.desc())
        )

        return list(result.scalars().all())

    @staticmethod
    async def end_session(
        db: AsyncSession,
        session: LearningSession,
    ) -> LearningSession:
        from datetime import datetime, timezone

        session.status = "completed"
        session.ended_at = datetime.now(timezone.utc)

        await db.commit()
        await db.refresh(session)

        return session
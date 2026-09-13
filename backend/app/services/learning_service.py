from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.agents.misconception.agent import detect_misconception
from app.agents.skill_detection.agent import detect_skill
from app.services.skill_service import SkillService
from app.services.user_skill_service import UserSkillService


class LearningService:

    @staticmethod
    async def process_analysis(
        db: AsyncSession,
        user_id: UUID,
        analysis: dict,
    ) -> dict:

        misconception = detect_misconception(
            analysis=analysis,
        )

        skill = detect_skill(
            dsa_concept=analysis.get("dsa_concept", ""),
        )

        user_skill = None

        if skill.skill != "Unknown":

            skill_record = await SkillService.get_skill_by_name(
                db,
                skill.skill,
            )

            if skill_record:

                user_skill = (
                    await UserSkillService.get_user_skill_by_skill(
                        db,
                        user_id,
                        skill_record.id,
                    )
                )

                if user_skill:
                    current = user_skill.proficiency

                    if misconception.has_misconception:
                        new_proficiency = max(
                            0.0,
                            current - 2.0,
                        )
                    else:
                        new_proficiency = min(
                            100.0,
                            current + 2.0,
                        )

                    user_skill = (
                        await UserSkillService.update_proficiency(
                            db,
                            user_id,
                            skill_record.id,
                            new_proficiency,
                        )
                    )

        return {
            "analysis": analysis,
            "misconception": misconception.model_dump(),
            "skill": skill.model_dump(),
            "user_skill": (
                {
                    "id": str(user_skill.id),
                    "skill_id": str(user_skill.skill_id),
                    "proficiency": user_skill.proficiency,
                }
                if user_skill
                else None
            ),
        }
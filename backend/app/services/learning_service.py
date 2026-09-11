from app.agents.misconception.agent import detect_misconception
from app.agents.skill_detection.agent import detect_skill


class LearningService:

    @staticmethod
    def process_analysis(
        analysis:dict,
    )->dict:

        misconception=detect_misconception(
            analysis
        )

        skill=detect_skill(
            analysis.get("dsa_concept","")
        )

        return{
            "analysis":analysis,
            "misconception":misconception.model_dump(),
            "skill":skill.model_dump()
        }
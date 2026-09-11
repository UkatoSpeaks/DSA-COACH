from pydantic import BaseModel


class SkillDetectionResult(BaseModel):
    skill:str
    confidence:float


def detect_skill(
        dsa_concept:str,
)-> SkillDetectionResult:

    concept=dsa_concept.strip()

    if not concept:
        return SkillDetectionResult(
            skill="Unknown",
            confidence=0.0
        )

    return SkillDetectionResult(
        skill=concept,
        confidence=1.0
    )
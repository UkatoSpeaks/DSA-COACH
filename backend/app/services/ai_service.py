from app.agents.code_analysis.agent import analyze_code


class AIService:

    @staticmethod
    async def analyze_submission(
        problem: str,
        code: str,
        language: str,
    ) -> dict:

        return await analyze_code(
            problem=problem,
            code=code,
            language=language,
        )
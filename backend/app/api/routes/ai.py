from fastapi import APIRouter
from app.agents.code_analysis.agent import analyze_code
from app.schemas.ai import CodeAnalysisRequest,CodeAnalysisResponse



router=APIRouter(
    prefix="/ai",
    tags=["AI"]
)


@router.post(
    "/analyze-code",
    response_model=CodeAnalysisResponse
)
async def analyze_code_endpoint(
    data: CodeAnalysisRequest
):
    analysis=await analyze_code(
        problem=data.problem,
        code=data.code,
        language=data.language
    )

    return CodeAnalysisResponse(
        analysis=analysis
    )
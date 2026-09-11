from pydantic import BaseModel, Field


class CodeAnalysisRequest(BaseModel):
    problem:str=Field(min_length=1)
    code: str=Field(min_length=1)
    language:str=Field(min_length=1)



class CodeAnalysisResult(BaseModel):
    correctness:str
    time_complexity:str
    space_complexity:str
    main_issue:str
    dsa_concept:str
    hint:str


class CodeAnalysisResponse(BaseModel):
    submission_id:str|None=None
    analysis:CodeAnalysisResult
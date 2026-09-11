from pydantic import BaseModel, Field


class CodeAnalysisRequest(BaseModel):
    problem:str=Field(min_length=1)
    code:str=Field(min_length=1)
    language:str=Field(min_length=1)



class CodeAnalysisResponse(BaseModel):
    analysis:str
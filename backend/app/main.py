from fastapi import FastAPI

from app.api.routes.users import router as users_router
from app.api.routes.problems import router as problems_router
from app.api.routes.skills import router as skills_router
from app.api.routes.user_skills import router as user_skills_router
from app.api.routes.submissions import router as submissions_router

app = FastAPI(
    title="AI DSA Coach",
    version="1.0.0",
)


app.include_router(users_router)
app.include_router(problems_router)
app.include_router(skills_router)
app.include_router(user_skills_router)
app.include_router(submissions_router)

@app.get("/")
async def root():
    return {
        "message": "AI DSA Coach API is running"
    }
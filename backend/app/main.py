from fastapi import FastAPI
from app.api.routes.users import router as users_router


app=FastAPI(
    title="AI DSA Coach",
    version="1.0.0"
)


app.include_router(users_router)



@app.get("/")
async def root():
    return{
        "message":"AI DSA Coach API is running"
    }
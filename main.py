from fastapi import FastAPI
from app.models.user import router as user_router
from app.models.task import router as task_router

app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(task_router, prefix="/tasks", tags=["Tasks"])

@app.get("/test-main")
async def test_main():
    return {"message": "Test route works"}


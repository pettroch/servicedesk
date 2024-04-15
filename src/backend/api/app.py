import uvicorn
from fastapi import FastAPI

from routers import (
    task_create,
    get_task,
    get_task_by_user,
    get_task_by_operator
)
from database import db


app = FastAPI()
app.include_router(task_create.router)
app.include_router(get_task.router)
app.include_router(get_task_by_user.router)
app.include_router(get_task_by_operator.router)


if __name__ == "__main__":
    db.create_db()
    uvicorn.run("app:app", port=5000, log_level="info")

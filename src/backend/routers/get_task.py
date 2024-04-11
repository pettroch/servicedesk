from fastapi import APIRouter
from pydantic import BaseModel

from database.models.task import Task
from database.db import session


router = APIRouter()

class task_model(BaseModel):
    task_id: int


@router.get("/api/task/get")
async def get(task: task_model):
    task_q = session.query(Task).filter_by(id=task.task_id).first()

    response = {
        "id": task_q.id,
        "name": task_q.name,
        "description": task_q.description,
        "creator_id": task_q.creator_id,
        "operator_id": task_q.operator_id,
        "date": task_q.date,
        "status_id": task_q.status_id
    }

    return response
